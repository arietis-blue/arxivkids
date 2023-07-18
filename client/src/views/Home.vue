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
          
          <!-- {{ fivePapersStore.fivePapers}} -->

          <!-- <div class="flex justify-center"> 上下两个的区别好好体会，怎么居中，居中的是什么 -->
          <div class="grid justify-items-center space-y-6">
            <!-- v-for显示10篇论文 -->
            <div v-for="paper in fivePapersStore.fivePapers" :key="paper.Paper_ID"
              class="w-2/3 my-2"
            >
              <PaperRow
                :Paper_ID="paper.Paper_ID"
                :Title_En="paper.Title_En"
                :Title_Ja="paper.Title_Ja"
                :Content_En="paper.Content_En"
                :Pdf_url="paper.Pdf_url"
                :Published="paper.Published"
                :Authors="paper.Authors"
              />
            </div>
          </div>
          
          



          <!-- <div class="flex">
            <PaperRow />
            <router-link to="login" class="w-full">
              <el-button type="warning" :icon="Star" circle />
            </router-link>
          </div> -->


        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>


<script setup>
import axios from 'axios'
// import { ref } from "vue";
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

import PaperRow from "../components/PaperRow.vue";
import { Star } from "@element-plus/icons-vue"



const goDetailPaper = () => {
  router.push('/detailpaper')
  // axios获取detailpaper的数据 访问后端api/paper
  // 加入historyList
}
</script>

<style scoped></style>
