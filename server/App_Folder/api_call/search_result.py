from pathlib import Path
from arxiv_api.arxiv_search import get_arxiv_data
from deepl_api.deepl import translate_ja_list


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
main('LLM cat:cs.CL')