# import sys
# import pandas as pd
# from pathlib import Path
from pdb import set_trace
from .operate_database import search_rank

def recommendation():
# 各個人のジャンルをもとに推薦
# ログインしていないなら、人気の論文表示
    user_id = -1
    # if(ログインしていたら):
    #     user_id = 000000000
    #     arxiv_data = (user_idの読んだ論文リスト)
    
    # ログインしていない場合
    if(user_id == -1):
        json_result = search_rank()
        return json_result["rank"]

    # else:
        # ジャンル抽出 カウント
        # キーワード抽出

        # query = ax.ArxivQuery()
        # query.max_results(10)
        # query.sortby("submittedDate")
        # query.sortorder("descending")
        # query.category("cs.LG").AND().abstract("deep learning")    