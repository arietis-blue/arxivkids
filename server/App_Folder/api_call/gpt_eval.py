import time
import concurrent.futures
import csv

from gpt_api.gpt_getkeywords import keywords,keywords_steps
from gpt_api.gpt_paraphrase import paraphrase
from deepl_api.deepl import translate_ja_list
from deepl_api.deepl import translate_ja
from arxiv_api.arxiv_search import get_arxiv_data
from deepl_api.deepl import translate_ja_list
from deepl_api.deepl import translate_ja


# キーワード取得を段階的に行う場合の処理(実験用)

# わざわざ main 関数を定義してその中に処理を書く
def main():
    paper_list = search('LLM')
    paper_list_new = []
    for paper in paper_list:
        time_sta = time.time()
        paper_json = detail(paper)
        time_end = time.time()
        paper_json["Time"] = (time_end- time_sta)
        paper_list_new.append(paper_json)
        print(paper_json["Content_Ja"])
        print(paper_json["Content_plain"])
    # CSVファイルに書き込むためのファイル名
    csv_filename = 'eval_result/output_4.csv'
    # CSVファイルを書き込みモードで開く
    with open(csv_filename, 'w+', newline='',encoding = 'utf-8') as csvfile:
        # CSVの列ヘッダーを定義
        fieldnames = list(paper_list[0].keys())
        # DictWriterオブジェクトを作成
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # 列ヘッダーを書き込む
        writer.writeheader()
        
        # JSONのリストをCSVに書き込む
        for paper in paper_list:
            writer.writerow(paper)

def detail_step(paper_json):
        content_ja = translate_ja(paper_json["Content_En"])
        paper_json["Content_Ja"] = content_ja

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # `paraphrase`関数を並列化して実行
            plain_content_future = executor.submit(paraphrase, content_ja)
            # `keywords`関数を並列化して実行
            keywords_future = executor.submit(keywords_steps, content_ja, paper_json["Categories"])

            # `paraphrase`関数の実行結果を取得
            plain_content = plain_content_future.result()
            paper_json["Content_plain"] = plain_content

            # `keywords`関数の実行結果を取得
            keyword_list = keywords_future.result()
            paper_json["Keywords"] = keyword_list
        return paper_json
    
def detail(paper_json):
        content_ja = translate_ja(paper_json["Content_En"])
        paper_json["Content_Ja"] = content_ja

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # `paraphrase`関数を並列化して実行
            plain_content_future = executor.submit(paraphrase, content_ja)
            # `keywords`関数を並列化して実行
            keywords_future = executor.submit(keywords, content_ja, paper_json["Categories"])

            # `paraphrase`関数の実行結果を取得
            plain_content = plain_content_future.result()
            paper_json["Content_plain"] = plain_content

            # `keywords`関数の実行結果を取得
            keyword_list = keywords_future.result()
            paper_json["Keywords"] = keyword_list
        return paper_json

def search(query):
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

if __name__ == "__main__":
    main()
    