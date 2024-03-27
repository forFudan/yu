export * from '../search/share'
import { ChaifenMap } from "../search/share";

export interface Card {
    /** 练习的题目 */
    name: string;
    /** 答案 */
    key: string;
}

export function find8relativeChars(zigen: string, chaifenMap: ChaifenMap) {
    let result = ''
    let count = 0
    for (const chaifen of chaifenMap.values()) {
        if (chaifen.division.includes(zigen)) {
            result += chaifen.char;
            count++;
            if (count >= 8) break;
        }
    }
    return result
}