from .arxiv_api.arxiv_search import get_arxiv_data
from .deepl_api.deepl import translate_ja_list
from .deepl_api.deepl import translate_ja

def main(query):
    # arxivから論文の取得
    paper_list = get_arxiv_data(query)
    title_list = [paper["Title_En"] for paper in paper_list]
    # タイトルをdeeplで翻訳
    title_ja_list = translate_ja_list(title_list)
    # "Title_Ja"として追加して返す
    for i,paper in enumerate(paper_list):
        paper["Title_Ja"] = title_ja_list[i]
    return(paper_list)

def get_papers(query):
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

# print(main('LLM cat:cs.CL'))
# papers = get_papers('LLM cat:cs.CL')
# print(add_ja_title(papers[0]))