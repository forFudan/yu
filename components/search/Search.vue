<script setup lang="ts">
import { shallowRef } from "vue";
import { watchThrottled, useUrlSearchParams } from "@vueuse/core";
import Card from "./Card.vue";
import { ChaifenMap, ZigenMap } from "./share";
const p = defineProps<{
    chaifenMap: ChaifenMap,
    zigenMap: ZigenMap,
    supplement: boolean,
}>()

const urlSearchParams = useUrlSearchParams()
const userInput = shallowRef(urlSearchParams?.q || '')
const searchZigens = shallowRef<string[]>()
watchThrottled(userInput, () => {
    const user = userInput.value as string
    urlSearchParams.q = user
    searchZigens.value = [...user].filter(zi => p.chaifenMap.has(zi))
}, { throttle: 300, immediate: true })

</script>

<template>
    <label class="input input-bordered bg-gray-100 dark:bg-slate-800 flex items-center gap-2 mt-8">
        <input type="text" class="grow" placeholder="输入文本查询宇浩拆分" v-model="userInput" />
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70">
            <path fill-rule="evenodd"
                d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
                clip-rule="evenodd" />
        </svg>
    </label>

    <div v-if="!userInput" class="opacity-40 text-center p-9 tracking-widest">少・顺・散・连・交・大</div>
    <div class="flex justify-center flex-wrap my-8" v-else>
        <Card v-for="zigen in searchZigens" :key="zigen" :chaifen="chaifenMap.get(zigen)" :zigenMap :supplement="p.supplement" />
    </div>

</template>