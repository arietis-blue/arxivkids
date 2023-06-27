# 環境変数にAPIキーを設定
import os
from dotenv import load_dotenv
import openai
import sys
from pathlib import Path
import json
import pandas as pd
import time

load_dotenv(Path(__file__).parent.parent.joinpath(".env"))
openai.api_key = os.environ["OPENAI_API_KEY"]

def paraphrase(content):
  time_sta = time.time()
  schema = {
    "type": "object",
    "properties": {
      "plain_abstract": { "type": "string" }
    },
    "required": ["plain_abstract"]
  }
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": "You are a professional translator."},
      {"role": "user", "content": "Please Explain it in a way that a non-specialist could understand in Japanese.\n"+ content}
    ],
    functions=[{"name": "set_plain_abstract", "parameters": schema}],
    function_call={"name": "set_plain_abstract"},
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


