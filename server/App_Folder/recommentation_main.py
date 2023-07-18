# import sys
# import pandas as pd
# from pathlib import Path
from pdb import set_trace
from .operate_database import search_rank


# 各個人のジャンルをもとに推薦
def recommendation():
    # user_idを-1で初期化
    user_id = -1
    # if(ログインしていたら):
    #     user_id = 000000000
    #     arxiv_data = (user_idの読んだ論文リスト)
    
    # ログインしていない場合、人気の論文を表示
    if(user_id == -1):
        json_result = search_rank()

        if json_result == {}: # 何も論文が検索されていないなら空列を返す
            return json_result
        else: # 論文が検索されていたらrankを返す
            return json_result["rank"]

    # else:
        # ジャンル抽出 カウント
        # キーワード抽出

        # query = ax.ArxivQuery()
        # query.max_results(10)
        # query.sortby("submittedDate")
        # query.sortorder("descending")
        # query.category("cs.LG").AND().abstract("deep learning")    