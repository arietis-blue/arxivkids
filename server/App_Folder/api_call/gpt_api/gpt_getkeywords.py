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
      "description": "Important Japanese keywords and their description.",
      "items": { 
          "keyword":{
            "keyword_title":{
              "type":"string",
              "description":"keyword name"
            },
            "keyword_description":{
              "type":"string",
              "description":"A 100-word sentence explaining the meaning of the KEYWORD"
            },
          }
                }
    }
  },
  "required": ["keyword_title","keyword_description"]
}  
  
  
  prompt = """
           Task: Please extract five technical terms about following paper and its description in Japanese. The description should be approximately 200 Japanese characters.
           Format example:
           [
             {
               'keyword_title':"keyword_1_title",
               'keyword_description':"keyword_1_description
             },
            {
               'keyword_title':"keyword_2_title",
               'keyword_description':"keyword_2_description
             },
            {
               'keyword_title':"keyword_3_title",
               'keyword_description':"keyword_3_description
             }
            ,,,
            {
               'keyword_title':"keyword_n_title",
               'keyword_description':"keyword_n_description
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
# Text = 'D-AgreeはBERTを用いたオンライン議論プラットフォームです。ファシリテーションエージェントが議論中の投稿をIBIS構造に基づき分類し、合意形成のための適切なファシリテーションを行います'
# keywords(Text)

