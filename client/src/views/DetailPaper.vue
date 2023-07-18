<template>
  <TopNav />

  <div class="common-layout pt-12">
    <el-container class="layout-container pt-12">
      <el-header class="layout-header">Title</el-header>
      <el-container class="inner-container">
        <el-aside class="aside-container" width="70%">
          <el-scrollbar height="100%">
            <div v-if="isWaiting">
              <el-progress :percentage="100" status="warning" :indeterminate="true" :duration="2" />
              <el-skeleton :rows="15" animated />
            </div>

            <div>
              <!-- {{ paperBody }} -->
              {{ allData }}
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
// const paperBody = ref("sdfdsfdf")
// const keyWords = ref([])

let isWaiting = ref(false)

//输出1,3,2 post前的命令执行完，不会等post，直接去执行post后面的
const getAll = () => {
  isWaiting.value = true
  // console.log(1)
  // axios.get('http://127.0.0.1:8000/api/arxiv/')
  axios.post('http://127.0.0.1:8000/api/paper/', {

    "Paper_ID": "http://arxiv.org/abs/2307.08678v1", "Title_En": "Do Models Explain Themselves? Counterfactual Simulatability of Natural Language Explanations", "Title_Ja": "モデルは自ら説明するか？自然言語による説明の反事実的シミュレーション可能性", "Authors": [ "Yanda Chen", "Ruiqi Zhong", "Narutatsu Ri", "Chen Zhao", "He He", "Jacob Steinhardt", "Zhou Yu", "Kathleen McKeown" ], "Categories": [ "Computation and Language", "Artificial Intelligence", "Machine Learning" ], "Published": "2023-07-17 17:41:47+00:00", "Content_En": "Large language models (LLMs) are trained to imitate humans to explain humandecisions. However, do LLMs explain themselves? Can they help humans buildmental models of how LLMs process different inputs? To answer these questions,we propose to evaluate $\\textbf{counterfactual simulatability}$ of naturallanguage explanations: whether an explanation can enable humans to preciselyinfer the model's outputs on diverse counterfactuals of the explained input.For example, if a model answers \"yes\" to the input question \"Can eagles fly?\"with the explanation \"all birds can fly\", then humans would infer from theexplanation that it would also answer \"yes\" to the counterfactual input \"Canpenguins fly?\". If the explanation is precise, then the model's answer shouldmatch humans' expectations. We implemented two metrics based on counterfactual simulatability: precisionand generality. We generated diverse counterfactuals automatically using LLMs.We then used these metrics to evaluate state-of-the-art LLMs (e.g., GPT-4) ontwo tasks: multi-hop factual reasoning and reward modeling. We found that LLM'sexplanations have low precision and that precision does not correlate withplausibility. Therefore, naively optimizing human approvals (e.g., RLHF) maynot be a sufficient solution.", "Pdf_url": "http://arxiv.org/pdf/2307.08678v1" 

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