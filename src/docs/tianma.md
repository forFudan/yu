<!-- omit in toc -->
# 天码

- [简介](#简介)
- [规则](#规则)
- [字根练习](#字根练习)

## 简介

天码是一个表形码输入方案，由宋天研制。特点有：四码定长、纯字形、双编码、繁简通打[^fanjian]等。因为其大码表形，小码取音的设计哲学，易学性极高。QQ讨论群：631302614

注意，本拆分查询中不显示首根小码补码。

<script setup>
import Search from '@/search/FetchSearch.vue'
import CharTrain from "@/train/CharTrain.vue"
import ZigenTrain from "@/train/ZigenTrain.vue"
</script>

<div class="tianma">
<Search chaifenUrl="/chaifen-tianma.csv" zigenUrl="/zigen-tianma.csv" :supplement="false" />
</div>

## 规则

天码共约 500 字根，归类后约 250，在 26 键上，依据其形态，对应到近似的拉丁字母上，形成规则排布。

::: tip 例
`人` `八` 像字母 A，故而排在 A 键上。
`丁` `下` `不` 像字母 T，故而排在 T 键上。
:::

每个字根还有一个小码，为其汉语拼音首字母。生僻字根或无读音字根小码为 v。

其编码规则类似于宇码，总结如下：

- 依次取首、次、三、末根
- 不足四码补末根小码（拼音）
- 仍不足四码补首根小码（若是 v 则可以省略）

::: info 编码规则公式化

单字拆分成若干字根后，最多取四根。假设首次三末根编码为 Aa Bb Cc Zz。则单字编码规则为：

- 单字根字 Zz
- 两字根字 AZza
- 三字根及以上字 ABCZ

单行定义为：ABCZza\[:4\]
:::

## 字根练习

<div class="tianma">
<ZigenTrain name="tianma" zigenUrl="/zigen-tianma.csv" :range="[0,]" mode='both' />
</div>

<!-- ## 单字练习

为了降低学习难度，练习中，不补首根小码。

<CharTrain name="tianma" zigenUrl="/zigen-tianma.csv" :range="[0,1000]" :supplement="false" /> -->

[^fanjian]: 一般认为单一码表繁简联合选重率小于万分之五十即具有繁简通打特性。