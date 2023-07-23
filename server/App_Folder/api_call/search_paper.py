import re

from .arxiv_api.arxiv_search import get_arxiv_data
from .deepl_api.deepl import translate_ja_list
from .deepl_api.deepl import translate_ja,translate_en

# クエリから論文検索
def get_papers(query):
    # 日本語のクエリは英語に
    if(contains_japanese(query)):
        query = translate_en(query)
        # print(f"translated query: {query}")
    # arxivから論文の取得
    paper_list = get_arxiv_data(query)
    return paper_list

# 論文のjsonを一つ受け取り、日本語のタイトルを追加する関数
def add_ja_title(paper):
    title = paper["Title_En"]
    # タイトルをdeeplで翻訳
    title_ja = translate_ja(title)
    # "Title_Ja"として追加して返す
    paper["Title_Ja"] = title_ja
    return(paper)

# 論文検索時の一連の処理をまとめる(使われていない)
def main(query):
    # 日本語のクエリは英語に
    if(contains_japanese(query)):
        query = translate_en(query)
        # print(f"translated query: {query}")
    # arxivから論文の取得
    paper_list = get_arxiv_data(query)
    title_list = [paper["Title_En"] for paper in paper_list]
    # タイトルをdeeplで翻訳
    title_ja_list = translate_ja_list(title_list)
    # "Title_Ja"として追加して返す
    for i,paper in enumerate(paper_list):
        paper["Title_Ja"] = title_ja_list[i]
    return(paper_list)

# 文字列が日本語を含むならTrueを返す
def contains_japanese(text):
    # 正規表現で日本語文字を検索
    return bool(re.search('[ぁ-んァ-ン一-龥]', text))

# print(main('LLM cat:cs.CL'))
# papers = get_papers('LLM cat:cs.CL')
# print(add_ja_title(papers[0]))
