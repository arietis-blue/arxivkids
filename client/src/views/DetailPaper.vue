<template>
  <TopNav />

  <div class="common-layout pt-12">
    <el-container class="layout-container pt-12">
      <el-header class="layout-header">Title</el-header>
      <el-container class="inner-container">
        <el-aside class="aside-container" width="70%">
          <el-scrollbar height="100%">
            <!-- <div v-if="isWaiting">
              <el-progress :percentage="100" status="warning" :indeterminate="true" :duration="2" />
              <el-skeleton :rows="15" animated />
            </div> -->

            <div>
              {{ paperBody }}
              <!-- {{ allData }} -->
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
              <div class="demo-collapse">
                <el-collapse v-model="activeNames" @change="handleChange">
                  <el-collapse-item title="Consistency" name="1">
                    <div>
                      Consistent with real life: in line with the process and logic of real
                      life, and comply with languages and habits that the users are used to;
                    </div>
                    <div>
                      Consistent within interface: all elements should be consistent, such
                      as: design style, icons and texts, position of elements, etc.
                    </div>
                  </el-collapse-item>
                  <el-collapse-item title="Feedback" name="2">
                    <div>
                      Operation feedback: enable the users to clearly perceive their
                      operations by style updates and interactive effects;
                    </div>
                    <div>
                      Visual feedback: reflect current state by updating or rearranging
                      elements of the page.
                    </div>
                  </el-collapse-item>
                  <el-collapse-item title="Efficiency" name="3">
                    <div>
                      Simplify the process: keep operating process simple and intuitive;
                    </div>
                    <div>
                      Definite and clear: enunciate your intentions clearly so that the
                      users can quickly understand and make decisions;
                    </div>
                    <div>
                      Easy to identify: the interface should be straightforward, which helps
                      the users to identify and frees them from memorizing and recalling.
                    </div>
                  </el-collapse-item>
                  <el-collapse-item title="Controllability" name="4">
                    <div>
                      Decision making: giving advices about operations is acceptable, but do
                      not make decisions for the users;
                    </div>
                    <div>
                      Controlled consequences: users should be granted the freedom to
                      operate, including canceling, aborting or terminating current
                      operation.
                    </div>
                  </el-collapse-item>
                </el-collapse>
              </div>

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
import '../mock/paper'

const allData = ref()
const paperBody = ref("sdfdsfdf")
const keyWords = ref([])

let isWaiting = ref(false)

//输出1,3,2 post前的命令执行完，不会等post，直接去执行post后面的
const getAll = () => {
  isWaiting.value = true
  // console.log(1)
  // axios.get('http://127.0.0.1:8000/api/arxiv/')
  axios.post('http://127.0.0.1:8000/api/paper/', {

    "Paper_ID": "http://arxiv.org/abs/2307.04744v1",
    "Title_En": "Behavioral Analysis of Pathological Speaker Embeddings of Patients During Oncological Treatment of Oral Cancer",
    "Content_En": "In this paper, we analyze the behavior of speaker embeddings of patientsduring oral cancer treatment. First, we found that pre- and post-treatmentspeaker embeddings differ significantly, notifying a substantial change invoice characteristics. However, a partial recovery to pre-operative voicetraits is observed after 12 months post-operation. Secondly, the same-speakersimilarity at distinct treatment stages is similar to healthy speakers,indicating that the embeddings can capture characterizing features of evenseverely impaired speech. Finally, a speaker verification analysis signifies astable false positive rate and variable false negative rate when combiningspeech samples of different treatment stages. This indicates robustness of theembeddings towards other speakers, while still capturing the changing voicecharacteristics during treatment. To the best of our knowledge, this is thefirst analysis of speaker embeddings during oral cancer treatment of patients.",
    "Categories": [
      "Audio and Speech Processing"
    ],
    "Authors": [
      "Jenthe Thienpondt",
      "Kris Demuynck"
    ],
    "Pdf_url": "http://arxiv.org/pdf/2307.04744v1",
    "Published": "2023-07-10T17:53:21Z",
    "Title_Ja": "口腔癌の腫瘍学的治療における患者の病理学的話者の埋め込みに関する行動分析"

  })
    .then(res => {
      // console.log(2)
      isWaiting.value = false
      console.log(res.data)
      allData.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  // console.log(3)
}
getAll()

const getPaperBody = () => {
  axios.post('api/papers/getBody')
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
  axios.get('api/paper/getKeywords').then(res => {
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
  height: 70vh;
  /* Adjust the height as needed */
  border-top: 1px solid #ccc;
}
</style>