import requests
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv(Path(__file__).parent.parent.joinpath(".env"))
API_KEY =os.environ["DEEPL_API_KEY"]# 自身の API キーを指定

# 英語の文字列のリストを受け取り、翻訳した文章を追加したリストとして返す
def translate_ja_list(content_list):
    # content_list = [article['Content_En'] for article in article_list] #articleの情報に訳をそのまま追加する場合
    # パラメータの指定
    params = {
                'auth_key' : API_KEY,
                'text' : content_list,
                'source_lang' : 'EN', # 翻訳対象の言語
                "target_lang": 'JA'  # 翻訳後の言語
            }
    # リクエストを投げる
    request = requests.post("https://api.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()
    result_list = [item['text'] for item in result["translations"]]
    return result_list

# 英語の文字列を受け取り、翻訳した文章を返す
def translate_ja(text):
    # パラメータの指定
    params = {
                'auth_key' : API_KEY,
                'text' : text,
                'source_lang' : 'EN', # 翻訳対象の言語
                "target_lang": 'JA'  # 翻訳後の言語
            }
    # リクエストを投げる
    request = requests.post("https://api.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()
    result = result["translations"][0]["text"]
    return result

# 日本語の文字列を受け取り、翻訳した英語の文章を返す
def translate_en(text):
    # パラメータの指定
    params = {
                'auth_key' : API_KEY,
                'text' : text,
                'source_lang' : 'JA', # 翻訳対象の言語
                "target_lang": 'EN'  # 翻訳後の言語
            }
    # リクエストを投げる
    request = requests.post("https://api.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()
    result = result["translations"][0]["text"]
    return result

# # Example Usage
# text = "Attention is all you need"
# text_list = ["Attention is all you need", "Automated facillitation agent", "Attention is all you need"]
# print(translate_ja_list(text_list))
# # print(translate_ja(text))