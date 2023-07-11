# 環境変数にAPIキーを設定
import os
from dotenv import load_dotenv
import openai
from pathlib import Path
import json
import time


load_dotenv(Path(__file__).parent.parent.joinpath(".env"))
openai.api_key = os.environ["OPENAI_API_KEY"]

# Textを受け取りキーワードと説明文のリストを返す
def keywords(content):
  time_sta = time.time()
  schema = {
  "type": "object",
  "properties": {
       "list": {
      "type": "array",
      "description": "Important Japanese keywords and their detailed description.",
      "items": { 
          "keyword":{
            "Keyword":{
              "type":"string",
              "description":"keyword name"
            },
            "Description":{
              "type":"string",
              "description":"200 Japanese Characters explaining the meaning of the KEYWORD"
            },
          }
                }
    }
  },
  "required": ["Keyword","Description"]
}  
  
  
  prompt = """
           Task: Please extract five technical terms about following paper and its detailed description in Japanese. 
           Limitation: each keyword description is in 200 Japanese Characters.
           Format example:
           [
             {
               'Keyword':"keyword_1_title",
               'Description':"keyword_1_description
             },
            {
               'Keyword':"keyword_2_title",
               'Description':"keyword_2_description
             },
            {
               'Keyword':"keyword_3_title",
               'Description':"keyword_3_description
             }
            ,,,
            {
               'Keyword':"keyword_n_title",
               'Description':"keyword_n_description
             }           ]
           """\
          + content

#出力
           
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": "You are an expert in the field of this paper."},
      {"role": "user", "content": prompt}
    ],
    functions=[{"name": "set_keywords_and_desctiption", "parameters": schema}],
    function_call={"name": "set_keywords_and_desctiption"},
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
  print(result)
  return(result)

# Example Usage
# Text = '我々は、高レベルのコミュニケーションと低レベルのパスプランニングの両方に、事前に訓練された大規模言語モデル（LLM）の力を活用する、マルチロボット協調のための新しいアプローチを提案する。ロボットは、タスク戦略を議論し、集団的に推論するためにLLMを装備している。LLMはサブタスク計画とタスク空間ウェイポイント経路を生成し、マルチアームモーションプランナーにより軌道計画を加速する。また、衝突チェックのような環境からのフィードバックを提供し、LLMエージェントがコンテキスト内で計画とウェイポイントを改善するように促す。評価のために、我々はRoCoBenchを導入する。RoCoBenchは、エージェントの表現と推論のためのテキストのみのデータセットとともに、幅広いマルチロボット協調シナリオをカバーする6タスクベンチマークである。RoCoBenchの全てのタスクにおいて高い成功率を達成し、タスクセマンティクスの変化にも適応する。我々のダイアログ設定は高い解釈性と柔軟性を提供し、実世界の実験では、RoCoは簡単にヒューマンインザループを組み込むことができ、ユーザはロボットエージェントとコミュニケーションし、協力してタスクを完了することができる。ビデオとコードはプロジェクトのウェブサイトhttps://project-roco.github.io'
# keywords(Text)

