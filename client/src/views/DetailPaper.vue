<template>
  <TopNav />

  <div class="common-layout pt-12">
    <el-container class="layout-container pt-10">
      <el-header class="layout-header" height="100px">
        <!-- Title -->
        <div class="font-bold text-2xl ml-4">{{ choosedPaperInfoStore.Title_En }}</div>
        <div class="font-semibold text-xl ml-4">{{ choosedPaperInfoStore.Title_Ja }}</div>
      </el-header>
      <el-container class="inner-container">
        <el-aside class="aside-container" width="70%">

          <!-- <el-scrollbar height="100%"> -->
          <div v-if="waitingPaper">
            <el-progress :percentage="100" status="warning" :indeterminate="true" :duration="2" />
            <el-skeleton :rows="30" animated />
          </div>


          <div class="mx-8 my-4">

            <el-tabs type="border-card">
              <el-tab-pane label="English Abstract">
                <div class="mt-3 text-lg mx-6 indent-8">
                  {{ currentDetailPaper.Content_En }}
                </div>
              </el-tab-pane>
              <el-tab-pane label="日本語の要旨">
                <div class="mt-3 text-lg mx-6 indent-8">
                  {{ currentDetailPaper.Content_Ja }}
                </div>
              </el-tab-pane>
              <el-tab-pane label="簡易な日本語" class="mt-3 text-lg mx-6 indent-8">
                {{ currentDetailPaper.Content_plain }}
              </el-tab-pane>
            </el-tabs>


            <!-- <div class="flex justify-end mb-2 ">
              <button class="rounded-l-full bg-red-500 text-black w-[80px] h-8 hover:bg-red-300" @click="chooseEN">
                English
              </button>
              <div class="h-8 w-0.5 bg-gray-300"></div>
              <button class="rounded-r-full bg-green-500 text-black w-[80px] h-8 hover:bg-green-300" @click="chooseJP">
                日本語
              </button>
            </div>

            <div class="mt-3 text-lg mx-6">
              <div v-if="showJP">
                {{ currentDetailPaper.Content_Ja }}
              </div>
              <div v-if="showEN">
                {{ currentDetailPaper.Content_En }}
              </div>
            </div> -->

            <!-- <div>{{ currentDetailPaper }}</div> -->

          </div>

          <!-- </el-scrollbar> -->
        </el-aside>

        <el-container class="main-footer-container">
          <el-main class="main-container space-y-2">
            <div>
              <span class="mr-4">{{ t('authors') }}:</span>
              <!-- {{ choosedPaperInfoStore.Authors }} -->
              <!-- bug:最后一个item会显示, -->
              <span v-for="name in choosedPaperInfoStore.Authors" :key="name" class="mr-2 text-blue-600">
                {{ name }},
              </span>
            </div>

            <div>
              <span class="mr-4">{{ t('published') }}:</span>
              <!-- {{ choosedPaperInfoStore.Published }} -->
              <span class="date">{{ formatDate(choosedPaperInfoStore.Published) }}</span>
            </div>

            <div>
              <span class="mr-4">{{ t('categories') }}:</span>
              <!-- {{ choosedPaperInfoStore.Categories }} -->
              <!-- bug:最后一个item会显示, -->
              <span v-for="Category in choosedPaperInfoStore.Categories" :key="Category" class="mr-2 ">
                {{ Category }},
              </span>
            </div>

            <div>
              <span class="mr-4">{{ t('download') }}:</span>
              <a :href="choosedPaperInfoStore.Pdf_url" target="_blank" class="underline decoration-dashed decoration-pink-600">[pdf]</a>
            </div>


          </el-main>

          <el-footer class="footer-container">
            <div v-if="waitingPaper">
              <el-skeleton :rows="30" animated />
            </div>
            <!-- {{ currentDetailPaper.Keywords }} -->
            <el-scrollbar height="100%">
              <!-- Keywords展示 -->
              <div class="demo-collapse mt-2">
                <el-collapse v-for="k_d in currentDetailPaper.Keywords" :key="k_d.Keyword">

                  <el-collapse-item>
                    <template #title>
                      <span class="text-lg">{{ k_d.Keyword }}</span>
                    </template>
                    <div class="text-base text-orange-600">
                      {{ k_d.Description }}
                    </div>
                  </el-collapse-item>

                </el-collapse>
              </div>


            </el-scrollbar>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>


<script setup>
import { ref } from "vue"
import axios from 'axios'
// import '../mock/paper'
import { useI18n } from 'vue-i18n'
const { t } =useI18n()

import { storeToRefs } from 'pinia'
import { useCurrentDetailPaperStore } from '../stores/currentDetailPaper'
// const { currentDetailPaper } = storeToRefs(useCurrentDetailPaperStore())

let revisit = localStorage.getItem('status');

let currentDetailPaper;
if (revisit == "false") {
  currentDetailPaper  = storeToRefs(useCurrentDetailPaperStore()).currentDetailPaper;
} else {
  currentDetailPaper = JSON.parse(localStorage.getItem('current_paper_detail'));
  // console.log(currentDetailPaper)
}

import { useWaitingStore } from '../stores/waiting'
const waitingStore = useWaitingStore()
const { waitingPaper } = storeToRefs(waitingStore)
//pinia的东西要是storeToRefs变成响应式的了，使用就要.value

import { useChoosedPaperInfoStore } from '../stores/choosedPaperInfo'


let choosedPaperInfoStore;
if (revisit == "false") {
  choosedPaperInfoStore = useChoosedPaperInfoStore();
  localStorage.setItem('current_paper', JSON.stringify(choosedPaperInfoStore));
  let revisit = "true";
  localStorage.setItem('status', revisit);
} else {
  choosedPaperInfoStore = JSON.parse(localStorage.getItem('current_paper'));
}


// const showJP = ref(true)
// const showEN = ref(false)
// const showCN = ref(false)

// const chooseJP = () => {
//   showJP.value = true
//   showEN.value = false
// }

// const chooseEN = () => {
//   showJP.value = false
//   showEN.value = true
// }

// const paperBody = ref("sdfdsfdf")
// const keyWords = ref([])

// const getPaperBody = () => {
//   axios.post('api/papers/getBody')
//     .then(res => {
//       console.log(res.data)
//       paperBody.value = res.data
//     })
//     .catch((err) => {
//       console.log(err)
//     })
// }
// getPaperBody()

// const getKeywords = () => {
//   axios.get('api/paper/getKeywords').then(res => {
//     console.log(res.data)
//     keyWords.value = res.data
//   })
//     .catch((err) => {
//       console.log(err);
//     });
// }
// getKeywords()

//输出1,3,2 post前的命令执行完，不会等post，直接去执行post后面的
// const getDetailPaper = () => {
//     // 确保 choosedPaperInfoStore 中的数据已经准备好
//     if (!choosedPaperInfoStore.Paper_ID || !choosedPaperInfoStore.Title_En || !choosedPaperInfoStore.Content_En) {
//       console.log("Missing required data in choosedPaperInfoStore.");
//       // return;
//     }
//     // axios获取detailpaper的数据 访问后端api/paper
//     waitingPaper.value = true
//     // console.log(1)
//     axios.post('http://127.0.0.1:8000/api/paper/', {
//         //又忘了.value了
//         "Paper_ID": choosedPaperInfoStore.Paper_ID,
//         "Title_En": choosedPaperInfoStore.Title_En,
//         "Title_Ja": choosedPaperInfoStore.Title_Ja,
//         "Authors": choosedPaperInfoStore.Authors,
//         "Categories": choosedPaperInfoStore.Categories,
//         "Published": choosedPaperInfoStore.Published,
//         "Content_En": choosedPaperInfoStore.Content_En,
//         "Pdf_url": choosedPaperInfoStore.Pdf_url
        
//         // "Paper_ID": "http://arxiv.org/abs/2304.01166v1",
//         // "Title_En": "Effective Feature Extraction for Intrusion Detection System using Non-negative Matrix Factorization and Univariate analysis",
//         // "Title_Ja": "非負行列因子化と単変量解析を用いた侵入検知システムのための効率的な特徴抽出",
//         // "Authors": [
//         //     "Swapnil Mane",
//         //     "Vaibhav Khatavkar",
//         //     "Niranjan Gijare",
//         //     "Pranav Bhendawade"
//         // ],
//         // "Categories": [
//         //     "Cryptography and Security"
//         // ],
//         // "Published": "2023-04-03 17:33:28+00:00",
//         // "Content_En": "An Intrusion detection system (IDS) is essential for avoiding maliciousactivity. Mostly, IDS will be improved by machine learning approaches, but themodel efficiency is degrading because of more headers (or features) present inthe packet (each record). The proposed model extracts practical features usingNon-negative matrix factorization and chi-square analysis. The more number offeatures increases the exponential time and risk of overfitting the model.Using both techniques, the proposed model makes a hierarchical approach thatwill reduce the features quadratic error and noise. The proposed model isimplemented on three publicly available datasets, which gives significantimprovement. According to recent research, the proposed model has improvedperformance by 4.66% and 0.39% with respective NSL-KDD and CICD 2017.",
//         // "Pdf_url": "http://arxiv.org/pdf/2304.01166v1"
    
//     })
//         .then(res => {
//             // console.log(2)
//             waitingPaper.value = false
//             console.log(res.data)
//             detailPaper.value = res.data
//         })
//         .catch((err) => {
//             console.log(err)
//         })
//     // console.log(3)
// }
// getDetailPaper()

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 10);
}

// setTimeout(_ => {alert(1)}, 1000)

</script>

<style scoped>
.date {
  font-size: 14px;
  color: #645e5e;
}

.layout-container {
  border: 1px solid #ccc;
}

.layout-header {
  border-bottom: 1px solid #ccc;
}

.inner-container {
  border: 1px solid #ccc;
}

.aside-container {
  border-right: 1px solid #ccc;
  height: 98vh;
  display: flex;
  flex-direction: column;
}

.main-footer-container {
  width: 30%;
  height: 98vh;
  display: flex;
  flex-direction: column;
  border-left: 1px solid #ccc;
}

.main-container {
  flex: 1;
  height: 30vh;
  border-bottom: 1px solid #ccc;
}

.footer-container {
  height: 70vh;
  /* Adjust the height as needed */
  border-top: 1px solid #ccc;
}
</style>