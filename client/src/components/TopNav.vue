<template>
  <div id="TopNav" class="fixed bg-neutral-700 mt-0.5 z-30 flex items-center w-full border-b h-[70px]">
    <div class="flex items-center justify-between w-full px-6 mx-auto">

      <router-link :to="{ name: 'Home' }">
        <img src="../assets/arxiv-logo-1-300x135.png" style="transform: scale(0.6);">
      </router-link>

      <div class="hidden md:flex items-center bg-[#F1F1F2] p-1 rounded-full max-w-[580px] w-full ">
        <input type="text"
          class="w-full pl-3 my-2 bg-transparent placeholder-[#838383] text-[15px] focus:outline-none text-black"
          v-model="searchContent" :placeholder="t('searchPapers')">
        <div class="px-3 py-1 flex items-center border-l border-l-gray-300">
          <el-button :icon="Search" circle @click="getFivePapers" />
        </div>
      </div>


      <div class="flex items-center justify-end gap-3 min-w-[275px] max-w-[350px] w-full">
        <!-- switch multi language -->
        <el-dropdown trigger="hover">
          <TranslateIcon :size="30" />
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="changeLanguage('en')">English</el-dropdown-item>
              <el-dropdown-item @click="changeLanguage('ja')">日本語</el-dropdown-item>
              <el-dropdown-item @click="changeLanguage('zh-cn')">中文</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>

        <!-- dark mode -->
        <div class="flex items-center mr-5">
          <button @click="toggleDark()" class="mr-1">
            <!-- <i inline-block align-middle i="dark:carbon-moon carbon-sun" /> -->
            <span class="">{{ isDark ? 'Dark' : 'Light' }}</span>
          </button>
          <el-switch v-model="isDark" class="" style="--el-switch-on-color: #2F4F4F; --el-switch-off-color: #D3D3D3"
            inline-prompt :active-icon="Sunny" :inactive-icon="Moon" size="large" />
        </div>

        <div v-if="!isLogined" class="flex items-center">
          <!-- <button @click="$generalStore.isLoginOpen = true" -->
          <button @click="isLoginOpenStore.isLoginOpen = true; isLogined = true"
            class="flex items-center bg-red-600 hover:bg-red-400 text-white font-semibold border rounded-md px-3 py-[6px] ring-2 ring-gray-300 hover:ring-4 hover:ring-red-300">
            <!-- <span class="mx-2 font-medium ">Log in</span> -->
            <span class="mx-2 font-medium ">{{ t('login') }}</span>
          </button>
        </div>

        <div v-else class="flex items-center">
          <div class="relative">
            <button class="mt-1" @click="showMenu = !showMenu">
              <img class="rounded-full" width="45" src="../assets/xjp.jpeg">
              <!-- :src="$userStore.image"> -->
            </button>

            <div v-if="showMenu" id="PopupMenu"
              class="absolute bg-white rounded-lg py-1 w-[140px] shadow-xl border top-[55px] -right-5">
              <router-link to="/profile/${$userStore.id}" @click="showMenu = false"
                class="flex items-center justify-start py-3 px-2 hover:bg-gray-100 cursor-pointer">
                <!-- <StarOutlineIcon :size="17" fillColor="#636363" class="ml-4" /> -->
                <AccountIcon :size="25" fillColor="#636363" />
                <span class="pl-2 font-semibold text-sm text-gray-700">Profile</span>
              </router-link>

              <div @click="logout"
                class="flex items-center justify-start py-3 px-1.5 hover:bg-gray-100 border-t cursor-pointer">
                <LogoutVariantIcon :size="25" fillColor="#636363" />
                <span class="pl-2 font-semibold text-sm">Log out</span>
              </div>

            </div>

          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
// import '../mock/arxiv'
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { storeToRefs } from 'pinia'
import { Search } from "@element-plus/icons-vue"
// npm i vue-material-design-icons后直接import
// 各种图标参见material https://pictogrammers.com/library/mdi/
import StarOutlineIcon from "vue-material-design-icons/StarOutline.vue";
import AccountIcon from "vue-material-design-icons/Account.vue";
import LogoutVariantIcon from "vue-material-design-icons/LogoutVariant.vue";
import TranslateIcon from "vue-material-design-icons/Translate.vue";

import { useI18n } from 'vue-i18n'
const { locale, t } =useI18n()
function changeLanguage(lang) {
  locale.value = lang
}

import { useDark, useToggle } from '@vueuse/core'
const isDark = useDark()
const toggleDark = useToggle(isDark)
import { Sunny, Moon } from '@element-plus/icons-vue'

import { useIsLoginOpenStore } from '../stores/isLoginOpen'
const isLoginOpenStore = useIsLoginOpenStore()

import { useFivePapersStore } from '../stores/fivePapers'
const fivePapersStore = useFivePapersStore()

import { useWaitingStore } from '../stores/waiting'
const waitingStore = useWaitingStore()
const { waitingArxiv } = storeToRefs(waitingStore)
//pinia的东西要是storeToRefs变成响应式的了，使用就要.value

import { useHasSearchedStore } from '../stores/hasSearched'
const { hasSearched } = storeToRefs(useHasSearchedStore())

const route = useRoute()
const router = useRouter()

let showMenu = ref(false)
let isLogined = ref(false)

const searchContent = ref("")
// const fivePapers = ref([])
// const fivePapers = ref()

//输出1,3,2 post前的命令执行完，不会等post，直接去执行post后面的
const getFivePapers = () => {
  router.push({ name: 'Home' })
  waitingArxiv.value = true //pinia的东西要是storeToRefs变成响应式的了，使用就要.value
  // console.log(1)
  console.log(searchContent)
  //别忘了script要value，之前"Search": searchContent就错了  有问题console.log()检查
  if (searchContent.value.trim() === "") {
    axios.get('http://127.0.0.1:8000/api/recommend/')
      .then(res => {
        waitingArxiv.value = false
        hasSearched.value = false
        console.log(res.data)
        fivePapersStore.fivePapers = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  else {
    axios.post('http://127.0.0.1:8000/api/arxiv/', { "Search": searchContent.value })
      .then(res => {
        // console.log(2)
        waitingArxiv.value = false
        hasSearched.value = true
        console.log(res.data)
        fivePapersStore.fivePapers = res.data //pinia的东西不用.value
      })
      .catch((err) => {
        console.log(err)
      })
  }
  // console.log(3)
}

// const goLogin = () => {
//   router.push('/login')
// }

const logout = () => {
  isLogined.value = false
  router.push({ name: 'Home' })
  try {
    // $userStore.logout()
  } catch (error) {
    console.log(error)
  }
}


</script>