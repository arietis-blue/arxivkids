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
           Task: Please extract five technical terms in Japanese. Then make descriptions for each technical term.
           Limit: Each description must be written in around 200 Japanese characters.
           Format example:
           {'list':[
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
             },
            ,,,
            {
               'Keyword':"keyword_n_name",
               'Description':"keyword_n_description
             }           ]}
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
    result_str = (completion.choices[0].message.function_call.arguments)
    result = json.loads(result_str)
    
    # 悪い例
    # result_str =""" {'list':[
    #   {'Keyword': 'keyword_1_name'},
    #   {'Keyword': 'keyword_2_name'},
    #   {'Keyword': 'keyword_3_name'},
    #   # ... 追加の要素
    #   {'Keyword': 'keyword_n_name'}
    # ]}"""
    # result = json.loads(result_str)
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
    # retry_prompt = f"""
    #         Task: Rewrite the following "Output" to a json list with 'Keyword' and 'Description' as elements, such as "Format example"."\n.
    #         "Output": \n{result_str}\n
    #         """
    # retry_prompt += """
    #        "Format example":
    #        [
    #          {
    #            'Keyword':"keyword_1_name",
    #            'Description':"keyword_1_description
    #          },
    #         {
    #            'Keyword':"keyword_2_name",
    #            'Description':"keyword_2_description
    #          },
    #         {
    #            'Keyword':"keyword_3_name",
    #            'Description':"keyword_3_description
    #          }
    #         ,,,
    #         {
    #            'Keyword':"keyword_n_name",
    #            'Description':"keyword_n_description
    #          }           ]
    #        """
    # completion = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo-0613",
    # messages=[
    #   {"role": "system", "content": "You are an expert in the following academic areas\n" + category_prompt},
    #   {"role": "user", "content": retry_prompt}
    # ],
    # functions=[{"name": "set_keywords_and_desctiption", "parameters": schema}],
    # function_call={"name": "set_keywords_and_desctiption"},
    # temperature=0,
    # )
    # result_str2 = (completion.choices[0].message.function_call.arguments)
    # result = json.loads(result_str2)
    # parser =  PydanticOutputParser(pydantic_object=Keywords)
    # new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
    # correct_result = (new_parser.parse(result_str))
    # print(correct_result)
    # result = json.loads(correct_result)
    # # それでもエラーが起きたらエラーを返す
    # # except:
    # #   print("error")
    # #   result = {
    # #         "Keyword": "GPT Error",
    # #         "Description": "GPT Error in Extracting Keyword. Please retry to get keyword."
    # #     }
    # result =  {
    #   'list':[{
    #         "Keyword": "GPT Error",
    #         "Description": "GPT Error in Extracting Keyword. Please retry to get keyword."
    #   }]}
      
  time_end = time.time()
  # 経過時間（秒）
  tim = time_end- time_sta
  print(f"keywords_time:{tim}")
  # print(result)
  return(result['list'])

# キーワードの一覧と説明を段階的に行う
def keywords_steps(content,category):
  time_sta = time.time()
  
  # キーワード取得
  # gptのfunction機能で指定する返り値の型
  name_schema = {
  "type": "object",
  "properties": {
       "list": {
      "type": "array",
      "description": "Important Japanese keywords and their detailed description.",
      "items": { 
            "Keyword":{
              "type":"string",
              "description":"keyword name"
            },
          }
    }
  },
  "required": ["Keyword"]
}  
  category_prompt = ",\n".join(category)
  
  prompt = """
           Task: Please extract five technical terms in Japanese.
           Format example:
           {'list':[
             {
               'Keyword':"keyword_1_name"
             },
            {
               'Keyword':"keyword_2_name"
             },
            {
               'Keyword':"keyword_3_name"
             },
            ,,,
            {
               'Keyword':"keyword_n_name"
             }           ]}
          Paper abstract:
           """\
          + content
  completion_name = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": "You are an expert in the following academic areas\n" + category_prompt},
      {"role": "user", "content": prompt}
    ],
    functions=[{"name": "set_keywords", "parameters": name_schema}],
    function_call={"name": "set_keywords"},
    temperature=0,
  )
  result_str_name = (completion_name.choices[0].message.function_call.arguments)

  
#説明文の作成
  description_schema = {
  "type": "object",
  "properties": {
       "list": {
      "type": "array",
      "description": "Description of Keywords",
      "items": { 
            "Description":{
              "type":"string",
              "description":"keyword description"
            },
          }
    }
  },
  "required": ["Description"]
  }       
  prompt = """
           Task: Please make descriptions for each five keywords in Japanese .
           Limit: Each description must be written in around 100 Japanese characters.
           Format example:
           {'list':[
             {
               'Description':"keyword_1_description"
             },
            {
               'Description':"keyword_2_description"
             },
            {
               'Description':"keyword_3_description"
             },
            ,,,
            {
               'Description':"keyword_n_description"
             }           ]}
          Keywords_list:
           """\
          + result_str_name
  completion_description = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": "You are an expert in the following academic areas\n" + category_prompt},
      {"role": "user", "content": prompt}
    ],
    functions=[{"name": "set_keywords_description", "parameters": description_schema}],
    function_call={"name": "set_keywords_description"},
    temperature=0,
  )
  result_str_description = (completion_description.choices[0].message.function_call.arguments)

  try:
    result_name = json.loads(result_str_name)
    result_description = json.loads(result_str_description)
        
    keyword_list = []
    
    for name, description in zip(result_name['list'],result_description['list']):
      keyword =  {
              "Keyword": name['Keyword'],
              "Description": description['Description']
              }
      keyword_list.append(keyword)
    # print(keyword_list)
    if(check_output_type(keyword_list)):
      None
    else:
      # jsonの型が正しくない場合はエラーを発生させ、型修正を行う
      raise Exception
  except:
    # エラー処理→langchainのParserを用いて出力の型を調整
    # try:
    print("json correction") 
    keyword_list = [{
            "Keyword": "GPT Error",
            "Description": "GPT Error in Extracting Keyword. Please retry to get keyword."
      }]
  time_end = time.time()
  # 経過時間（秒）
  tim = time_end- time_sta
  print(f"time to get keywords: {tim}")
  # print(result)
  return(keyword_list)

# 出力の型が正しいかチェックする
def check_output_type(json_list):
    for item in json_list:
        if 'Keyword' not in item or 'Description' not in item:
            return False
    return True

# Example Usage
# Text = '自律走行車の知覚・制御システムは、科学的にも産業的にも活発な研究分野である。このような機能を実現するには、適切なアルゴリズムと適切なコンピューティングプラットフォームが必要である。本論文では、MultiTaskV3detection-segmentationネットワークを、単一のアーキテクチャで両方の機能を実行できる知覚システムの基礎として使用した。このネットワークは適切に訓練され、定量化され、AMD Xilinx Kria KV260 Vision AIembeddedプラットフォーム上に実装された。このデバイスを使用することで、計算の並列化と高速化が可能になった。さらに、システム全体の消費電力は、CPUベースの実装に比べて比較的小さく（弱いCPUの最低消費電力55ワットに対し、平均5ワット）、プラットフォームのサイズが小さい（119mm×140mm×36mm）ため、利用可能なスペースが限られている機器でも使用できます。また、物体検出ではmAP（平均平均精度）の97％以上、画像セグメンテーションではmIoU（平均交差和）の90％以上の精度を達成している。本稿では、提案されたソリューションを模擬都市でテストするために使用されたMecanumホイール・ビークルの設計についても詳述する'
# category = [
#         "Computer Vision and Pattern Recognition",
#         "Image and Video Processing"
#     ]
# output = keywords(Text,category)
# print(output)