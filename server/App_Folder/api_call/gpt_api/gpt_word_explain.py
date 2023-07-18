# 環境変数にAPIキーを設定
import os
from dotenv import load_dotenv
import openai
from pathlib import Path
import json
import time

load_dotenv(Path(__file__).parent.parent.joinpath(".env"))
openai.api_key = os.environ["OPENAI_API_KEY"]

# テキストを受け取って平易に言い換えたテキストを返す
def explain_by_ja(query,category,content):
  time_sta = time.time()
  schema = {
    "type": "object",
    "properties": {
      "word_explanation": { "type": "string" }
    },
    "required": ["word_explanation"]
  }
  
  category_prompt = ",\n".join(category)
  main_prompt = f"Explain the meaning of the term '{query}' in Japanese. Please consider following paper abstract.\n{content}"
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
     # {"role": "system", "content": "You are a professional university teacher."},
      {"role": "system", "content": "You are an expert in the following academic areas\n" + category_prompt},
      {"role": "user", "content": main_prompt}
    ],
    functions=[{"name": "set_word_explanation", "parameters": schema}],
    function_call={"name": "set_word_explanation"},
    temperature=0,
  )
  try:
    result = json.loads(completion.choices[0].message.function_call.arguments)
  except:
    print("error")
    result = "gpt error"
    print(completion.choices[0].message.function_call.arguments)
    
  time_end = time.time()
  # 経過時間（秒）
  tim = time_end- time_sta
  print(tim)
  # print(result)
  return(result["word_explanation"])

# # test case 
# Query = '大規模言語モデル'
# print(explain_by_ja(Query))
# Content = "我々は、高レベルのコミュニケーションと低レベルのパスプランニングの両方に、事前に訓練された大規模言語モデル（LLM）の力を活用する、マルチロボット協調のための新しいアプローチを提案する。ロボットは、タスク戦略を議論し、集団的に推論するためにLLMを装備している。LLMはサブタスク計画とタスク空間ウェイポイント経路を生成し、マルチアームモーションプランナーにより軌道計画を加速する。また、衝突チェックのような環境からのフィードバックを提供し、LLMエージェントがコンテキスト内で計画とウェイポイントを改善するように促す。評価のために、我々はRoCoBenchを導入する。RoCoBenchは、エージェントの表現と推論のためのテキストのみのデータセットとともに、幅広いマルチロボット協調シナリオをカバーする6タスクベンチマークである。RoCoBenchの全てのタスクにおいて高い成功率を達成し、タスクセマンティクスの変化にも適応する。我々のダイアログ設定は高い解釈性と柔軟性を提供し、実世界の実験では、RoCoは簡単にヒューマンインザループを組み込むことができ、ユーザはロボットエージェントとコミュニケーションし、協力してタスクを完了することができる。ビデオとコードはプロジェクトのウェブサイトhttps://project-roco.github.io"
# Text = 'large language model'
# category = [
#         "Robotics",
#         "Artificial Intelligence",
#         "Machine Learning"
#     ]
# output = explain_by_ja(Text,category,Content)
# print(output)
