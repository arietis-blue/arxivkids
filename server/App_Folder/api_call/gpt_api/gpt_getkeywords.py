# 環境変数にAPIキーを設定
import os
from dotenv import load_dotenv
import openai
from pathlib import Path
import json
import time
# langchainを用いた型エラー訂正のためのライブラリ群
from langchain.output_parsers import PydanticOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import OutputFixingParser
from pydantic import BaseModel
from typing import List


load_dotenv(Path(__file__).parent.parent.joinpath(".env"))
openai.api_key = os.environ["OPENAI_API_KEY"]

# 型エラー訂正のためのテンプレートの型
class Keyword(BaseModel):
    Keyword: str
    Description: str

class Keywords(BaseModel):
  list: List[Keyword]
  
# Textを受け取りキーワードと説明文のリストを返す
def keywords(content,category):
  time_sta = time.time()
  # gptのfunction機能で指定する返り値の型
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
              "description":"200 Japanese Characters explaining the meaning of the Keyword"
            },
          }
                }
    }
  },
  "required": ["Keyword","Description"]
}  
  category_prompt = ",\n".join(category)
  
  prompt = """
           Task: Please extract five technical term and create a description for that keyword in Japanese. I would like to acquire and explain technical terms so that beginners can understand the following paper. Please add an explanation of the word itself as well as how it is used in the abstract.
           Limit: Each description must be written in around 200 Japanese characters.
           Format example:
           [
             {
               'Keyword':"keyword_1_name",
               'Description':"keyword_1_description
             },
            {
               'Keyword':"keyword_2_name",
               'Description':"keyword_2_description
             },
            {
               'Keyword':"keyword_3_name",
               'Description':"keyword_3_description
             }
            ,,,
            {
               'Keyword':"keyword_n_name",
               'Description':"keyword_n_description
             }           ]
          Paper abstract:
           """\
          + content

#出力
           
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": "You are an expert in the following academic areas\n" + category_prompt},
      {"role": "user", "content": prompt}
    ],
    functions=[{"name": "set_keywords_and_desctiption", "parameters": schema}],
    function_call={"name": "set_keywords_and_desctiption"},
    temperature=0.5,
  )
  try:
    result = json.loads((completion.choices[0].message.function_call.arguments))
    
    # 悪い例
    # result =""" {'list':[
    #   {'Keyword': 'keyword_1_name'},
    #   {'Keyword': 'keyword_2_name'},
    #   {'Keyword': 'keyword_3_name'},
    #   # ... 追加の要素
    #   {'Keyword': 'keyword_n_name'}
    # ]}"""
    # print(result['list'])
    if(check_output_type(result['list'])):
      None
    else:
      # jsonの型が正しくない場合はエラーを発生させ、型修正を行う
      raise Exception
  except:
    # エラー処理→langchainのParserを用いて出力の型を調整
    # try:
    print("json correction")
    result =  {
      'list':[{
            "Keyword": "GPT Error",
            "Description": "GPT Error in Extracting Keyword. Please retry to get keyword."
      }]}
    
    # parser =  PydanticOutputParser(pydantic_object=Keywords)
    # new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
    # print(result)
    # correct_result = (new_parser.parse(result))
    # print(correct_result)
    # result = json.loads(correct_result)
    # # それでもエラーが起きたらエラーを返す
    # # except:
    # #   print("error")
    # #   result = {
    # #         "Keyword": "GPT Error",
    # #         "Description": "GPT Error in Extracting Keyword. Please retry to get keyword."
    # #     }
      
  time_end = time.time()
  # 経過時間（秒）
  tim = time_end- time_sta
  print(tim)
  # print(result)
  return(result)

# 出力の型が正しいかチェックする
def check_output_type(json_list):
    for item in json_list:
        if 'Keyword' not in item or 'Description' not in item:
            return False
    return True

# Example Usage
# Text = '我々は、高レベルのコミュニケーションと低レベルのパスプランニングの両方に、事前に訓練された大規模言語モデル（LLM）の力を活用する、マルチロボット協調のための新しいアプローチを提案する。ロボットは、タスク戦略を議論し、集団的に推論するためにLLMを装備している。LLMはサブタスク計画とタスク空間ウェイポイント経路を生成し、マルチアームモーションプランナーにより軌道計画を加速する。また、衝突チェックのような環境からのフィードバックを提供し、LLMエージェントがコンテキスト内で計画とウェイポイントを改善するように促す。評価のために、我々はRoCoBenchを導入する。RoCoBenchは、エージェントの表現と推論のためのテキストのみのデータセットとともに、幅広いマルチロボット協調シナリオをカバーする6タスクベンチマークである。RoCoBenchの全てのタスクにおいて高い成功率を達成し、タスクセマンティクスの変化にも適応する。我々のダイアログ設定は高い解釈性と柔軟性を提供し、実世界の実験では、RoCoは簡単にヒューマンインザループを組み込むことができ、ユーザはロボットエージェントとコミュニケーションし、協力してタスクを完了することができる。ビデオとコードはプロジェクトのウェブサイトhttps://project-roco.github.io'
# category = [
#         "Robotics",
#         "Artificial Intelligence",
#         "Machine Learning"
#     ]
# output = keywords(Text,category)
# print(output)
