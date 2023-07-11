<template>
  <TopNav />

  <div class="common-layout pt-12">
    <el-container class="layout-container pt-12">
      <el-header class="layout-header">Title</el-header>
      <el-container class="inner-container">
        <el-aside class="aside-container" width="70%">
          <el-scrollbar height="100%">
            <div>
              {{ paperBody }}
            </div>
          </el-scrollbar>
        </el-aside>

        <el-container class="main-footer-container">
          <el-main class="main-container">
            author date
          </el-main>
          <el-footer class="footer-container">
            {{ keyWords }}
            <el-scrollbar height="100%">
                <div class="mb-4">
                 <KeywordRow />
                </div>
                <div class="mb-4">
                  <KeywordRow />
                </div>
                <div class="mb-4">
                    <KeywordRow />
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

const paperBody = ref("sdfdsfdf")
const keyWords = ref([])

const getPaperBody = () => {
  axios.get('api/papers/getBody')
    .then(res => {
    console.log(res.data)
    paperBody.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}
getPaperBody()


const getKeywords = () => {
  axios.get('api/papers/getKeywords').then(res => {
    console.log(res.data)
    keyWords.value = res.data
  })
    .catch((err) => {
      console.log(err);
    });
}
getKeywords()


</script>

<style scoped>
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
  height: 70vh; /* Adjust the height as needed */
  border-top: 1px solid #ccc;
}


</style>