<template>
  <TopNav />

  <div class="common-layout pt-[100px]">
    <el-container class="layout-container">
      <el-container class="inner-container">
        <el-aside class="aside-container" width="70%">
          <el-scrollbar height="100%">
            <p v-for="item in 30" :key="item" class="scrollbar-demo-item">{{ item }}</p>
                <PaperRow />
                <PaperRow />
                <PaperRow />
                <PaperRow />
                <PaperRow />
          </el-scrollbar>
        </el-aside>

        <el-container class="main-footer-container">
          <el-main class="main-container">
            Main
          </el-main>
          <el-footer class="footer-container">
            <el-scrollbar height="100%">
<!--            <p v-for="item in 20" :key="item" class="scrollbar-demo-item">{{ item }}</p>-->
                <PaperRow />
                <PaperRow />
                <PaperRow />
                <PaperRow />
                <PaperRow />
            </el-scrollbar>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
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

<style scoped>
.layout-container {
  border: 1px solid #ccc;
}


.inner-container {
  border: 1px solid #ccc;
}

.aside-container {
  border-right: 1px solid #ccc;
  height: 98vh;
}

.main-footer-container {
  width: 30%;
  display: flex;
  flex-direction: column;
  border-left: 1px solid #ccc;
}

.main-container {
  flex: 1;
  border-bottom: 1px solid #ccc;
}

.footer-container {
  height: 50vh; /* Adjust the height as needed */
  border-top: 1px solid #ccc;
}

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
