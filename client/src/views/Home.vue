<template>
  <TopNav />

  <div class="bg-neutral-700 py-3 mt-4 flex justify-between items-center w-full border-b h-[70px]">
    <img src="../assets/arxiv-logo-1-300x135.png" style="transform: scale(0.6);">

    <div class="hidden md:flex items-center bg-[#F1F1F2] p-1 rounded-full max-w-[580px] w-full ">
      <input type="text" class="w-full pl-3 my-2 bg-transparent placeholder-[#838383] text-[15px] focus:outline-none"
        placeholder="Search papers">
      <div class="px-3 py-1 flex items-center border-l border-l-gray-300">
        <el-button :icon="Search" circle />
      </div>
    </div>

    <div class="mr-3 flex justify-end">
      <button
        class="bg-red-600 hover:bg-red-400 text-white font-semibold py-2 px-4 rounded ring-2 ring-gray-300 hover:ring-4 hover:ring-cyan-300"
        @click="goLogin">
        Login
      </button>
      <el-icon color="#409EFC" :size="50"><MoreFilled /></el-icon>
    </div>

    

  </div>





  <PaperRow />
  <PaperRow />
  <PaperRow />

  
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
// import TopNav from '../components/TopNav.vue'
import PaperRow from "../components/PaperRow.vue";

import { Search } from "@element-plus/icons-vue"

const route = useRoute()
const router = useRouter()

const goLogin = () => {
  router.push('/login')
}

</script>