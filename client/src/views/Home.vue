<template>
  <TopNav />
  <!-- <AuthOverlay v-if="isLoginOpenStore.isLoginOpen" /> -->
  <!-- 用了storeToRefs所以可以不用写前面的isLoginOpenStore.了 -->
  <AuthOverlay v-if="isLoginOpen" />

  <div class="items-center">
    <el-container>
      <el-header>
        <!-- <TopNav /> -->
      </el-header>
      <el-main>
        <el-scrollbar height="800px" class="mt-4">

          <div v-if="waitingArxiv">
            <!-- <el-progress :percentage="100" status="warning" :indeterminate="true" :duration="1" /> -->
            <el-skeleton :rows="30" animated />
          </div>

          <!-- fixed固定住，不会随着scrollなくなる -->
          <div class="fixed flex flex-col justify-start mx-2 space-y-6">
            <div class="rounded bg-gradient-to-r from-gray-100 to-gray-200 w-[160px] h-[40px] flex items-center justify-center">
              <span v-show="!hasSearched" class="text-[15px] font-bold bg-clip-text text-transparent bg-gradient-to-r from-gray-600 to-gray-600">Recommend for you</span>
              <span v-show="hasSearched" class="text-[15px] font-bold text-gray-600">Search result</span>
            </div>

            <el-switch
              v-model="omitAbstract"
              class="mb-2"
              style="--el-switch-on-color: #b91026; --el-switch-off-color: #c99898"
              active-text="Show abstracts"
              inactive-text="Hide abstracts"
            />
          </div>
          
          <!-- {{ fivePapersStore.fivePapers}} -->

          <!-- <div class="flex justify-center"> 上下两个的区别好好体会，怎么居中，居中的是什么 -->
          <div class="grid justify-items-center space-y-6">
            <!-- v-for显示10篇论文 -->
            <div v-for="paper in fivePapersStore.fivePapers" :key="paper.Paper_ID"
              class="flex items-center space-x-3"
            >
              <PaperRow
                :Paper_ID="paper.Paper_ID"
                :Title_En="paper.Title_En"
                :Title_Ja="paper.Title_Ja"
                :Content_En="paper.Content_En"
                :Pdf_url="paper.Pdf_url"
                :Published="paper.Published"
                :Authors="paper.Authors"
                :Categories="paper.Categories"
              />

              <button class="p-2 rounded-full bg-gray-300 hover:p-2.5"
                @click="like"
              >
                <HeartIcon :size="25" :fillColor=iconColor />
              </button>

            </div>
          </div>


        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>


<script setup>
import axios from 'axios'
import { ref } from "vue"
import { useRoute, useRouter } from "vue-router"
const route = useRoute()
const router = useRouter()

import { storeToRefs } from 'pinia'
import { useIsLoginOpenStore } from '../stores/isLoginOpen'
const isLoginOpenStore = useIsLoginOpenStore()
// 用storeToRefs解构出来，依然保持是响应式的变量，这样使用时可以不用写xxxStore.xxx，直接xxx就好了
//其实准确来说不写xxxStore.xxx主要是 const {xxx} = xxxStore，但这样ref的状态是不会响应改变的，所以还需要storeToRefs，如果它是需要响应的变量
//具体还是参考pinia的英语文档
const { isLoginOpen } = storeToRefs(isLoginOpenStore)

import { useFivePapersStore } from '../stores/fivePapers'
const fivePapersStore = useFivePapersStore()

import { useWaitingStore } from '../stores/waiting'
const waitingStore = useWaitingStore()
const { waitingArxiv } = storeToRefs(waitingStore)

import { useOmitAbstractStore } from '../stores/omitAbstract'
const omitAbstractStore = useOmitAbstractStore()
const { omitAbstract } = storeToRefs(omitAbstractStore)

import { useHasSearchedStore } from '../stores/hasSearched'
const { hasSearched, isFirstTimeAccess } = storeToRefs(useHasSearchedStore())

import PaperRow from "../components/PaperRow.vue";
import { Star } from "@element-plus/icons-vue"
// npm i vue-material-design-icons后直接import
// 各种图标参见material https://pictogrammers.com/library/mdi/
import HeartIcon from "vue-material-design-icons/Heart.vue";

let iconColor = ref("#636363")

const like = () => {
  if(iconColor.value === "#636363"){
    iconColor.value = "#ff1493"
  }
  else{
    iconColor.value = "#636363"
  }
  isLoginOpen.value = true
}

// isFirstTimeAccess 写在home的话每次跳到/都会重新赋值为true
// 故isFirstTimeAccess必须是全局的
const firstTimeGetRecommendedPapers = () => {
  axios.get('http://127.0.0.1:8000/api/recommend/')
    .then(res => {
      console.log(res.data)
      fivePapersStore.fivePapers = res.data
    })
    .catch((err) => {
      console.log(err)
    })

    isFirstTimeAccess.value = false
}

if(isFirstTimeAccess.value){
  firstTimeGetRecommendedPapers()
}


// alert('wtf')

</script>

<style scoped></style>
