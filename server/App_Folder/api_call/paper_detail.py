from .gpt_api.gpt_getkeywords import keywords,keywords_steps
from .gpt_api.gpt_paraphrase import paraphrase
from .deepl_api.deepl import translate_ja_list
from .deepl_api.deepl import translate_ja

import concurrent.futures

# # 論文のjsonを受け取り、Content_Ja, (Keywords)を追加
# # 並列処理をしないバージョン
# def main(paper_json):
#     # 要約の日本語訳
#     content_ja = translate_ja(paper_json["Content_En"])
#     paper_json["Content_Ja"] = content_ja
#     # 平易な言葉に言い換え
#     plain_content = paraphrase(content_ja)
#     paper_json["Content_plain"] = plain_content
#     # キーワードの取得
#     # 日本語訳に対してキーワードの取得
#     keywords_json = keywords(content_ja,paper_json["Categories"])
#     keyword_list = keywords_json["list"]
#     paper_json["Keywords"] = keyword_list
#     return paper_json

# "平易な言葉の言い換え"と"キーワード取得"の並列実行
def main(paper_json):
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
            keywords_json = keywords_future.result()
            keyword_list = keywords_json["list"]
            paper_json["Keywords"] = keyword_list
        return paper_json
    
# Test Usage
# import search_paper
# import time
# time_sta = time.time()
# paper_sample = {
#     "Paper_ID": "http://arxiv.org/abs/2307.08670v1",
#     "Title_En": "Age of Gossip on a Grid",
#     "Content_En": "We consider a gossip network consisting of a source generating updates and$n$ nodes connected in a two-dimensional square grid. The source keeps updatesof a process, that might be generated or observed, and shares them with thegrid network. The nodes in the grid network communicate with their neighborsand disseminate these version updates using a push-style gossip strategy. Weuse the version age metric to quantify the timeliness of information at thenodes. We find an upper bound for the average version age for a set of nodes ina general network. Using this, we show that the average version age at a nodescales as $O(n^{\\frac{1}{3}})$ in a grid network. Prior to our work, it hasbeen known that when $n$ nodes are connected on a ring the version age scalesas $O(n^{\\frac{1}{2}})$, and when they are connected on a fully-connected graphthe version age scales as $O(\\log n)$. Ours is the first work to show an agescaling result for a connectivity structure other than the ring andfully-connected networks that represent two extremes of network connectivity.Our work shows that higher connectivity on a grid compared to a ring lowers theage experience of each node from $O(n^{\\frac{1}{2}})$ to $O(n^{\\frac{1}{3}})$.",
#     "Categories": [
#         "Information Theory",
#         "Multiagent Systems",
#         "Networking and Internet Architecture",
#         "Signal Processing",
#         "Information Theory"
#     ],
#     "Authors": [
#         "Arunabh Srivastava",
#         "Sennur Ulukus"
#     ],
#     "Pdf_url": "http://arxiv.org/pdf/2307.08670v1",
#     "Published": "2023-07-17T17:33:10Z",
#     "Title_Ja": "グリッド上のゴシップの時代"
# }

# new_paper = main(paper_sample)
# print(new_paper)
# time_end = time.time()
# # 経過時間（秒）
# tim = time_end- time_sta
# print(tim)
