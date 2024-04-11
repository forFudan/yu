<script setup lang="ts">
import { shallowRef } from "vue";
import { onMounted } from "vue";
import { watchThrottled, useUrlSearchParams } from "@vueuse/core";
import Chaifen from "./Chaifen.vue";
import { fetchCsvAsMap } from "../search/share";

const p = defineProps<{
    chars: string,
}>()

interface ChaifenPlot {
    char: string,
    parts: string,
    colors: string,
}

type ChaifenPlotMap = Map<string, ChaifenPlot>
const chaifenPlotMap = shallowRef<ChaifenPlotMap>()
const searchChaifenPlots = shallowRef<string[]>()

async function fetchChaifenPlot(url: string) {
    return await fetchCsvAsMap(url) as unknown as ChaifenPlotMap
}

onMounted(async () => {
    if (chaifenPlotMap.value) return;
    chaifenPlotMap.value = await fetchChaifenPlot("/chaifen_plot.csv")
    // searchChaifenPlots.value = [...p.chars].filter(zi => chaifenPlotMap.has(zi))
})

</script>

<template>
    <Chaifen v-for="item in  [...'的']" char='的' parts='5 2 1' />
    <Chaifen v-for="item in  [...'的']" char='的' :parts='[5, 2, 1]' />
    <Chaifen v-for=" item  in   [...'的']" :char='item' :parts='chaifenPlotMap?.get(item).parts.split(" ")' />
    <p v-for="  item   in   [...p.chars]  " :key='item'> {{ item === "的" }} </p>
    <p v-for="  item   in   [...p.chars]  " :key='item'> {{ chaifenPlotMap?.get(item).parts === "5 2 1" }} </p>
    <p v-for="  item   in   [...p.chars]  " :key='item'> {{ chaifenPlotMap?.get(item).parts }} </p>
    <p v-for="  item   in   [...p.chars]  " :key='item'> {{ chaifenPlotMap?.get(item).colors }} </p>
    <!-- <div>
        <Chaifen v-for='item in [...p.chars]' :key='item' :char='item' :parts="chaifenPlotMap?.get(item).parts"
            :colors="chaifenPlotMap?.get(item).colors">
        </Chaifen>
    </div>
    <div> {{ typeof chaifenPlotMap }}</div>
    <div> {{ [...p.chars] }} </div>
    <div> {{ chaifenPlotMap?.get("的").parts }} </div>
    <div> {{ searchChaifenPlots }} </div> -->
</template>

<script lang="ts">

</script>