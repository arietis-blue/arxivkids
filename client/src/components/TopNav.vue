<template>
  <div id="TopNav" class="fixed bg-neutral-700 mt-3 z-30 flex items-center w-full border-b h-[70px]">
    <div class="flex items-center justify-between w-full px-6 mx-auto">

      <img src="../assets/arxiv-logo-1-300x135.png" style="transform: scale(0.6);">


      <div class="hidden md:flex items-center bg-[#F1F1F2] p-1 rounded-full max-w-[580px] w-full ">
        <input type="text" class="w-full pl-3 my-2 bg-transparent placeholder-[#838383] text-[15px] focus:outline-none"
          placeholder="Search papers">
        <div class="px-3 py-1 flex items-center border-l border-l-gray-300">
          <el-button :icon="Search" circle />
        </div>
      </div>


      <div class="flex items-center justify-end gap-3 min-w-[275px] max-w-[320px] w-full">
        <div v-if="!isLogined" class="flex items-center">
          <!-- <button @click="$generalStore.isLoginOpen = true" -->
          <button
            @click="isLogined = true"
            class="flex items-center bg-red-600 hover:bg-red-400 text-white font-semibold border rounded-md px-3 py-[6px] ring-2 ring-gray-300 hover:ring-4 hover:ring-red-300">
            <span class="mx-2 font-medium ">Log in</span>
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
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { Search } from "@element-plus/icons-vue"
// npm i vue-material-design-icons后直接import
// 各种图标参见material https://pictogrammers.com/library/mdi/
import StarOutlineIcon from "vue-material-design-icons/StarOutline.vue";
import AccountIcon from "vue-material-design-icons/Account.vue";
import LogoutVariantIcon from "vue-material-design-icons/LogoutVariant.vue";

const route = useRoute()
const router = useRouter()

let showMenu = ref(false)
let isLogined = ref(false)

const goLogin = () => {
  router.push('/login')
}

const logout = () => {
  isLogined.value = false
  router.push('/')
  try {
    $userStore.logout()
  } catch (error) {
    console.log(error)
  }
}

</script>