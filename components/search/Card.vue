<script setup lang="ts">
//@ts-nocheck
import ZitongLogo from "./assets/zitong.svg";
import YedianLogo from "./assets/yedian.png";
import CtextLogo from "./assets/ctext.png";
import HandianLogo from "./assets/handian.png";
import { computed } from "vue";
import { Chaifen, ZigenMap, makeCodesFromDivision } from "./share";

const p = defineProps<{
    chaifen: Chaifen,
    zigenMap: ZigenMap,
    supplement: boolean,
}>()

const uriText = computed(() => encodeURIComponent(p.chaifen.char))
const unicode = computed(() => p.chaifen.char.charCodeAt(0).toString(16).toUpperCase())

const codes = computed(() => makeCodesFromDivision(p.chaifen.division, p.zigenMap, p.supplement))

const codes_tw = computed(() => p.chaifen.division_tw == '' ? '' : makeCodesFromDivision(p.chaifen.division_tw, p.zigenMap))

</script>

<template>
    <div class="group border p-3 m-2 rounded-3xl shadow-md zigen-font text-center bg-gray-50 dark:bg-slate-900">
        <div class="text-4xl text-indigo-800 dark:text-indigo-300">{{ chaifen.char }}</div>
        <div class="opacity-0 justify-center group-hover:opacity-70 transition text-sm">{{ chaifen.region }}</div>
        <!-- <div class="opacity-70 justify-center transition text-sm">{{ chaifen.region }}</div> -->

        <div class="flex flex-col" v-if="codes_tw == ''">
            <div class="text-indigo-800 dark:text-indigo-300 text-xl">{{ chaifen.division }}</div>
            <div class="font-mono tracking-widest">{{ codes }}</div>
        </div>

        <div class="flex" v-else>
            <div class="flex flex-col">
                <div class="text-indigo-800 dark:text-indigo-300">{{ chaifen.division }}</div>
                <div class="font-mono tracking-widest">{{ codes }}</div>
            </div>
            <div class="flex flex-col ml-3 tooltip font-sans" data-tip="臺灣標準字形拆分">
                <div class="text-indigo-800 dark:text-indigo-300 zigen-font">{{ chaifen.division_tw }}</div>
                <div class="font-mono tracking-widest">{{ codes_tw }}</div>
            </div>
        </div>



        <div class="invisible group-hover:visible">
            <div class="flex justify-center dark:opacity-55 opacity-100">
                <a :href="'https://zi.tools/zi/' + uriText" class="" target="_blank" rel="noreferrer" title="字统网查询">
                    <img :src=ZitongLogo alt="字统网" width="22" />
                </a>
                <a :href="'http://www.yedict.com/zscontent.asp?uni=' + unicode" class="" target="_blank"
                    rel="noreferrer" title="叶典网查询">
                    <img :src="YedianLogo" alt="叶典网" width="22" />
                </a>
                <a :href="'https://www.zdic.net/hans/' + uriText" class="" target="_blank" rel="noreferrer"
                    title="汉典查询">
                    <img :src="HandianLogo" alt="汉典网" width="22" />
                </a>
                <a :href="'https://ctext.org/dictionary.pl?if=gb&char=' + uriText" class="" target="_blank"
                    rel="noreferrer" title="中國哲學書電子化計劃查询">
                    <img :src="CtextLogo" alt="中國哲學書電子化計劃" width="22" />
                </a>
            </div>
        </div>
    </div>
</template>