<template>
    <!-- PaperRow -->
    <!-- w-[1060px]不固定的话，有些paper会不知道为什么超级宽 -->
    <div class="w-[850px] my-2 overflow-hidden flex flex-col justify-between rounded-2xl shadow-2xl  hover:ring-2 ring-gray-500
        border-b hover:border-t hover:border-y-2 hover:border-x cursor-pointer"
        :class="[omitAbstract ? 'h-[260px]' : 'h-[160px]']"
        :style="{ backgroundColor: getRandomLightColor() }"
    >

        <div class="mx-2 flex -mb-1">
            <div class="mr-2">{{ Paper_ID }}</div>
            
            <a :href="Pdf_url" target="_blank" class="underline decoration-dashed decoration-pink-600">
                <el-icon><Link /></el-icon>
                [pdf]
            </a>
        </div>

        <div class="flex flex-col justify-center items-center text-xl hover:italic" :style="{ backgroundColor: getRandomLightColor() }"
            @click="goDetailPaper"
        >
            <div class="mr-3 font-bold text-gray-950">{{ Title_En }}</div>
            <div class="font-semibold text-gray-800">{{ Title_Ja }}</div>
        </div>
        
        <div v-show="omitAbstract" class="px-6">
            <el-scrollbar height="90px">
                <p class="text-gray-700 text-base font-semibold">
                    {{  Content_En }}
                </p>
            </el-scrollbar>
        </div>
            
        <div class="ml-1 truncate">
            <span class="mr-2">Authors:</span>
            {{ Authors }}
        </div>
        <div class="flex mx-2 -mt-3">
            <span class="mr-2">Submitted:</span>
            <p class="date">{{ formatDate(Published) }}</p>
        </div>
    </div>
</template>

<script setup>
import { defineProps, toRefs, ref } from "vue"
import { useRoute, useRouter } from "vue-router"
const route = useRoute()
const router = useRouter()
import axios from 'axios'
import { storeToRefs } from 'pinia'

const props = defineProps({
    Paper_ID: String,
    Title_En: String,
    Title_Ja: String,
    Authors: Array,
    Published: String,
    Content_En: String,
    Pdf_url: String,
    Categories: Array
})

const { Paper_ID, Title_En, Title_Ja, Authors, Published, Content_En, Pdf_url, Categories } = toRefs(props);

import { useOmitAbstractStore } from '../stores/omitAbstract'
// const omitAbstractStore = useOmitAbstractStore()
const { omitAbstract } = storeToRefs(useOmitAbstractStore())

import { useWaitingStore } from '../stores/waiting'
const waitingStore = useWaitingStore()
const { waitingPaper } = storeToRefs(waitingStore)
//pinia的东西要是storeToRefs变成响应式的了，使用就要.value

// import { useCurrentDetailPaperStore } from '../stores/currentDetailPaper'
// const { currentDetailPaper } = storeToRefs(useCurrentDetailPaperStore())

import { useChoosedPaperInfoStore } from '../stores/choosedPaperInfo'
const choosedPaperInfoStore = useChoosedPaperInfoStore()

function getRandomLightColor() {
    return "hsl(" + Math.random() * 360 + ", 100%, 75%)";
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toISOString().slice(0, 10);
}

//输出1,3,2 post前的命令执行完，不会等post，直接去执行post后面的
const goDetailPaper = () => {
    // router.push('/detailpaper')
    // axios获取detailpaper的数据 访问后端api/paper
    // waitingPaper.value = true
    // console.log(1)
    // axios.post('http://127.0.0.1:8000/api/paper/', {
    //     //又忘了.value了
    //     "Paper_ID": Paper_ID.value,
    //     "Title_En": Title_En.value,
    //     "Title_Ja": Title_Ja.value,
    //     "Authors": Authors.value,
    //     "Categories": Categories.value,
    //     "Published": Published.value,
    //     "Content_En": Content_En.value,
    //     "Pdf_url": Pdf_url.value
        
        // "Paper_ID": "http://arxiv.org/abs/2304.01166v1",
        // "Title_En": "Effective Feature Extraction for Intrusion Detection System using Non-negative Matrix Factorization and Univariate analysis",
        // "Title_Ja": "非負行列因子化と単変量解析を用いた侵入検知システムのための効率的な特徴抽出",
        // "Authors": [
        //     "Swapnil Mane",
        //     "Vaibhav Khatavkar",
        //     "Niranjan Gijare",
        //     "Pranav Bhendawade"
        // ],
        // "Categories": [
        //     "Cryptography and Security"
        // ],
        // "Published": "2023-04-03 17:33:28+00:00",
        // "Content_En": "An Intrusion detection system (IDS) is essential for avoiding maliciousactivity. Mostly, IDS will be improved by machine learning approaches, but themodel efficiency is degrading because of more headers (or features) present inthe packet (each record). The proposed model extracts practical features usingNon-negative matrix factorization and chi-square analysis. The more number offeatures increases the exponential time and risk of overfitting the model.Using both techniques, the proposed model makes a hierarchical approach thatwill reduce the features quadratic error and noise. The proposed model isimplemented on three publicly available datasets, which gives significantimprovement. According to recent research, the proposed model has improvedperformance by 4.66% and 0.39% with respective NSL-KDD and CICD 2017.",
        // "Pdf_url": "http://arxiv.org/pdf/2304.01166v1"
    
    // })
    //     .then(res => {
    //         // console.log(2)
    //         waitingPaper.value = false
    //         console.log(res.data)
    //         currentDetailPaper.value = res.data
    //     })
    //     .catch((err) => {
    //         console.log(err)
    //     })
    // console.log(3)

    //已经入手的数据先展示在detailpaper上
    choosedPaperInfoStore.Title_En = Title_En.value
    choosedPaperInfoStore.Title_Ja = Title_Ja.value
    choosedPaperInfoStore.Authors = Authors.value
    choosedPaperInfoStore.Published = Published.value
    choosedPaperInfoStore.Categories = Categories.value
    choosedPaperInfoStore.Pdf_url = Pdf_url.value
    choosedPaperInfoStore.Paper_ID = Paper_ID.value
    choosedPaperInfoStore.Content_En = Content_En.value
    //为什么Pdf_url在F12中查看是undefined???
    // 答：そもそもapi/recommend/就没有返回pdf_url；如果是搜索出来的paper点进去没问题的
    console.log(Pdf_url.value)
    console.log(choosedPaperInfoStore.Pdf_url)
    console.log(Categories.value)

    router.push('/detailpaper')

    // 加入historyList
}

</script>

<style scoped>
.date {
  font-size: 14px;
  color: #645e5e;
}
</style>