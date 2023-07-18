<template>
    <!-- PaperRow -->
    <div class="w-full h-[260px] overflow-hidden flex flex-col justify-between rounded-2xl shadow-2xl  hover:ring-2 ring-gray-500
        border-b hover:border-t hover:border-y-2 hover:border-x cursor-pointer"
        :style="{ backgroundColor: getRandomLightColor() }">

        <div class="mx-2 flex -mb-1">
            <div class="mr-2 underline decoration-indigo-500">{{ Paper_ID }}</div>
            <el-icon><Link /></el-icon>
            <a :href="Pdf_url" style="text-decoration: underline;">[pdf]</a>
        </div>

        <div class="flex flex-col justify-center items-center text-xl hover:italic" :style="{ backgroundColor: getRandomLightColor() }">
            <div class="mr-3 font-bold text-gray-950">{{ Title_En }}</div>
            <div class="font-semibold text-gray-800">{{ Title_Ja }}</div>
        </div>

        
        <div class="px-6">
            <el-scrollbar height="100px">
                <p class="text-gray-700 text-base font-semibold">
                    {{  Content_En }}
                </p>
            </el-scrollbar>
        </div>
        
        <div class="ml-1 truncate">
            <span class="mr-2">Authors:</span>
            {{ Authors }}
        </div>
        <div class="flex mx-2 -mt-5">
            <span class="mr-2">Submitted:</span>
            <p class="date">{{ formatDate(Published) }}</p>
        </div>
    </div>
</template>

<script setup>
import { defineProps, toRefs, ref } from "vue"

const props = defineProps({
    Paper_ID: String,
    Title_En: String,
    Title_Ja: String,
    Authors: Array,
    Published: String,
    Content_En: String,
    Pdf_url: String,
})

const { Paper_ID, Title_En, Title_Ja, Authors, Published, Content_En, Pdf_url } = toRefs(props);

function getRandomLightColor() {
    return "hsl(" + Math.random() * 360 + ", 100%, 75%)";
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toISOString().slice(0, 10);
}

</script>

<style scoped>
.date {
  font-size: 14px;
  color: #645e5e;
}
</style>