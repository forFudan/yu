export * from '../train/share'
import { withBase } from 'vitepress'
import * as vue from 'vue'

//#region 输入法的规则
export interface ImeRule {
    /** 顶屏时 取前几码的首选字 */
    pop: number
    /** 最大码长 */
    len: number
    /** 空码自动上屏码长 */
    autoCm: number
    /** 首选上屏键 */
    cm1: string
    /** 次选上屏键 */
    cm2: string
    /** 三选上屏键 */
    cm3: string
    /** 编码用的键位 */
    keys: 26 | 27
}

export const YuhaoRule: ImeRule = {
    pop: 0,
    len: 4,
    autoCm: 5,
    cm1: ' ',
    cm2: ';',
    cm3: "'",
    keys: 26,
}
//#endregion

//#region 读取码表
export interface MabiaoItem {
    name: string,
    key: string,
}


const mabiaoCache = {}


/** 下载进度条 */
interface IProgress {
    max: number;
    current: number;
}

export async function fetchMabiao(url: string, progressRef: vue.Ref<IProgress>) {
    if (url in mabiaoCache) return mabiaoCache[url];

    try {
        const res = await fetch(withBase(url))
        if (!res.ok) throw new Error();

        //  响应头没有文件体积,就假装是 2MiB 
        progressRef.value.max = Number(res.headers.get('Content-Length') || 2 << 20)

        let received = 0
        progressRef.value.current = received
        let chunks: Uint8Array[] = [];

        const reader = res.body.getReader();
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            chunks.push(value);
            received += value.length;
            progressRef.value.current = received
        }

        let allChunks = new Uint8Array(received);
        let position = 0;
        for (const chunk of chunks) {
            allChunks.set(chunk, position);
            position += chunk.length;
        }
        let text = new TextDecoder("utf-8").decode(allChunks);

        const result: MabiaoItem[] = []
        for (const line of text.trim().split('\n')) {
            const lineTuple = line.trim().split('\t')
            result.push({ name: lineTuple[1], key: lineTuple[0] })
        }

        // 必须要排序
        result.sort(sortFunc)
        mabiaoCache[url] = result
        return result
    } catch (error) {
        if (error instanceof Error)
            alert(`无法下载或解析《${url}》文件：${error.cause}`)
        throw error
    }
}
//#endregion


//#region 查找候选词条
export function compareTwoStrings(a: string, b: string) {
    if (a === b) return 0
    if (a < b) return -1
    return 1
}

/** 根据编码的长度和编码内容排序 */
export function sortFunc(a: MabiaoItem, b: MabiaoItem) {
    return compareTwoStrings(a.key, b.key)
}

/** 
 * 二分查找法，锁定上下界.
 * 例如：找到ab词条, 会找到一个范围, 范围内所有词条的编码的前缀都是ab, 像是 ab abc abz
 * 
 * @param arr 排序好的拆分数据卡片
 * @param keyPrefix 搜索的编码的前缀
 * @returns 一对数, 表示上下边界的前闭后开区间. 空码返回null
 */
export function biSearchBetween(arr: MabiaoItem[], keyPrefix: string) {
    // console.log('biSearchBetween', keyPrefix);
    if (keyPrefix === '') return [0, arr.length]
    // 找上边界
    const topBoundary = biSearchPoint(arr, keyPrefix, 0, compareTopBoundary)
    if (topBoundary < 0)
        throw new Error(`cannot find prefix(top) ${keyPrefix}`)

    // 找下边界
    const botBoundary = biSearchPoint(arr, keyPrefix, topBoundary, compareBotBoundary)
    // 报错唯一的可能是出现空码
    if (botBoundary < 0)
        return null

    return [topBoundary, botBoundary] as const
}

export function searchTop(arr: MabiaoItem[], keyPrefix: string) {
    const topBoundary = biSearchPoint(arr, keyPrefix, 0, compareTopBoundary)
    if (topBoundary < 0) return null
    if (!arr[topBoundary].key.startsWith(keyPrefix)) return null
    return topBoundary
}

/** 返回 -1 说明 码表里不可能找得到 */
function biSearchPoint(arr: MabiaoItem[], keyPrefix: string, topIndex: number, compareFunc: typeof compareTopBoundary) {
    // 检查上边界
    let top = topIndex
    const topCompare = compareFunc(arr, keyPrefix, top)
    if (topCompare === 0) return top
    if (topCompare < 0) return -1

    // 检查下边界情况
    let bot = arr.length - 1
    const botCompare = compareFunc(arr, keyPrefix, bot)
    if (botCompare === 0) return bot + 1
    if (botCompare > 0) return -1

    // 中点
    let point = top + ((bot - top) / 2) | 0
    let compare = compareFunc(arr, keyPrefix, point)

    while (compare !== 0) {
        if (bot - top === 1) {
            return bot
        }

        if (compare > 0) {
            top = point
        } else {
            bot = point
        }
        point = top + ((bot - top) / 2) | 0
        compare = compareFunc(arr, keyPrefix, point)
        // console.log(top, bot, point, compare, arr[point].key);
    }
    return point
}

/** 对于上边界, 一定要找到相邻两行, 一行不是前缀, 一行是前缀 */
function compareTopBoundary(arr: MabiaoItem[], keyPrefix: string, index: number) {
    const indexIsPrefix = cardIsPrefix(arr[index], keyPrefix)
    const previousIndexIsPrefix = (index === 0) ? false : cardIsPrefix(arr[index - 1], keyPrefix)
    if (indexIsPrefix) {
        if (previousIndexIsPrefix) {
            //两行都是前缀, 要向上找
            return -1
        } else {
            // 上一行不是, 这一行是, 就是要锁定的
            return 0
        }
    } else {
        if (previousIndexIsPrefix) {
            // 这一行不是前缀, 但上一行是, 这是下边界, 要向上找
            return -1
        } else {
            // 都不是前缀, 不知前后, 只能通过字符串比较
            return compareTwoStrings(keyPrefix, arr[index].key)
        }
    }
}

/** 对于下边界, 一定要找到相邻两行, 上一行是前缀, 这一行不是前缀 */
function compareBotBoundary(arr: MabiaoItem[], keyPrefix: string, index: number) {
    const indexIsPrefix = cardIsPrefix(arr[index], keyPrefix)
    // 最后一行是前缀, 则必然锁定
    if (indexIsPrefix && index === arr.length - 1) { return 0 }

    const previousIndexIsPrefix = (index === 0) ? false : cardIsPrefix(arr[index - 1], keyPrefix)
    if (indexIsPrefix) {
        // 这一行是前缀, 那么无论如何, 都要向下寻找
        return 1
    } else {
        if (previousIndexIsPrefix) {
            // 上一行是前缀, 这一行不是, 就是锁定的
            return 0
        } else {
            // 都不是前缀, 不知前后, 只能通过字符串比较
            return compareTwoStrings(keyPrefix, arr[index].key)
        }
    }
}

function cardIsPrefix(card: MabiaoItem, prefix: string) {
    return card.key.startsWith(prefix, 0)
}
//#endregion