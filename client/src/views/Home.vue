<template>
  <TopNav />
  <AuthOverlay v-if="isLoginOpenStore.isLoginOpen" />
  <div class="common-layout">
    <el-container>
      <el-header>
        <!-- <TopNav /> -->
      </el-header>
      <el-main>
        <el-scrollbar height="800px" class="mt-4">
          {{ fivePapersStore.fivePapers }}
          <PaperRow />
          <PaperRow />
          <PaperRow />
          <PaperRow />
          <div class="flex">
            <PaperRow />
            <router-link to="login" class="w-full">
              <el-button type="warning" :icon="Star" circle />
            </router-link>
          </div>
          
          <p v-for="item in 20" :key="item" class="scrollbar-demo-item">{{ item }}</p>
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>


<script setup>
import axios from 'axios'
// import { ref } from "vue";
import { useIsLoginOpenStore } from '../stores/isLoginOpen'
const isLoginOpenStore = useIsLoginOpenStore()
import { useFivePapersStore } from '../stores/fivePapers'
const fivePapersStore = useFivePapersStore()

import PaperRow from "../components/PaperRow.vue";
import { Star } from "@element-plus/icons-vue"
</script>

<style scoped>
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
</style>
