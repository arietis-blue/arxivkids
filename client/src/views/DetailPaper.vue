<template>
  <TopNav />

  <div class="common-layout pt-12">
    <el-container class="layout-container pt-10">
      <el-header class="layout-header">
        <!-- Title -->
        <div class="font-bold text-2xl">{{ choosedPaperInfoStore.Title_En }}</div>
        <div class="font-semibold text-xl">{{ choosedPaperInfoStore.Title_Ja }}</div>
      </el-header>
      <el-container class="inner-container">
        <el-aside class="aside-container" width="70%">

          <!-- <el-scrollbar height="100%"> -->
          <div v-if="waitingPaper">
            <el-progress :percentage="100" status="warning" :indeterminate="true" :duration="2" />
            <el-skeleton :rows="30" animated />
          </div>

          <div class="mx-4 my-4">

            <div class="flex justify-end mb-2 ">
              <button class="rounded-l-full bg-red-500 text-black w-[80px] h-8 hover:bg-red-300"
                @click="chooseEN"
              >
                English
              </button>
              <div class="h-8 w-0.5 bg-gray-300"></div>
              <button class="rounded-r-full bg-green-500 text-black w-[80px] h-8 hover:bg-green-300"
                @click="chooseJP"
              >
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
            </div>

            <!-- <div>{{ currentDetailPaper }}</div> -->

          </div>

          <!-- </el-scrollbar> -->
        </el-aside>

        <el-container class="main-footer-container">
          <el-main class="main-container">
            <div>
              <span class="mr-4">Authors:</span>
              <!-- {{ choosedPaperInfoStore.Authors }} -->
              <!-- bug:最后一个item会显示, -->
              <span v-for="name in choosedPaperInfoStore.Authors" :key="name" class="mr-2 text-blue-600">
                {{ name }},
              </span>
            </div>

            <div>
              <span class="mr-4">Published:</span>
              <!-- {{ choosedPaperInfoStore.Published }} -->
              <span class="date">{{ formatDate(choosedPaperInfoStore.Published) }}</span>
            </div>

            <div>
              <span class="mr-4">Categories:</span>
              <!-- {{ choosedPaperInfoStore.Categories }} -->
              <!-- bug:最后一个item会显示, -->
              <span v-for="Category in choosedPaperInfoStore.Categories" :key="Category" class="mr-2 ">
                {{ Category }},
              </span>
            </div>

            <div>
              <span class="mr-4">Download:</span>
              <a :href="choosedPaperInfoStore.Pdf_url" class="underline decoration-dashed decoration-pink-600">[pdf]</a>
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
                    <div class="text-base">
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
import { storeToRefs } from 'pinia'
import { useCurrentDetailPaperStore } from '../stores/currentDetailPaper'
const { currentDetailPaper } = storeToRefs(useCurrentDetailPaperStore())

import { useWaitingStore } from '../stores/waiting'
const waitingStore = useWaitingStore()
const { waitingPaper } = storeToRefs(waitingStore)
//pinia的东西要是storeToRefs变成响应式的了，使用就要.value

import { useChoosedPaperInfoStore } from '../stores/choosedPaperInfo'
const choosedPaperInfoStore = useChoosedPaperInfoStore()

const showJP = ref(true)
const showEN = ref(false)
const showCN = ref(false)

const chooseJP = () => {
  showJP.value = true
  showEN.value = false
}

const chooseEN = () => {
  showJP.value = false
  showEN.value = true
}

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