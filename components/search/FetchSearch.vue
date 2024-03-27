<script setup lang="ts">
import { onMounted, shallowRef } from "vue";
import Search from "./Search.vue";
import { ZigenMap, ChaifenMap, fetchChaifen, fetchZigen } from "./share";

const p = defineProps<{
    zigenUrl: string,
    supplement: boolean,
}>()

const chaifenMap = shallowRef<ChaifenMap>()
const zigenMap = shallowRef<ZigenMap>()

onMounted(() => {
    Promise.all([fetchChaifen('/chaifen.csv'), fetchZigen(p.zigenUrl)])
        .then((v) => {
            chaifenMap.value = v[0]
            zigenMap.value = v[1]
        })
})
</script>

<template>
    <div class="text-gray-600" v-if="!zigenMap">正在加载拆分数据……</div>
    <Search v-else :chaifenMap :zigenMap :supplement />
</template>