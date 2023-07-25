from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .api_call import search_paper, paper_detail
from .operate_database import search_titles, search_papers, add_title, add_content_keywords, delete
from .recommentation_main import recommendation
from pdb import set_trace
from django.shortcuts import render, redirect


def view_one(request):
    # ビュー関数でセッションに値をセット
    
    # print("come to view1")
    # print(request.session["Paper_detail"])
    return redirect('paper')


# Arxiv_Searchのgetメソッドを用いたDebug用 
search = {
    "Search": "LLM cat:cs.CL"
}

# Create your views here.
class Arxiv_Search(APIView):
    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)
        # return Response(search_paper.main(search["Search"]))
    
    def post(self, request, *args, **kwargs):
        search_word = request.data
        # return Response(search_paper.main(search_word["Search"]))

        search_result_list = search_paper.get_papers(search_word['Search'])

        # 5つの論文の検索結果を返す
        search_list = []
        for paper in search_result_list:
            # Paper_IDを取得
            paper_id = paper["Paper_ID"]
        

            # 既に論文があればそのまま取得、なければ空のjson(=まだ検索されたことのない論文)を返す。
            paper_json = search_titles(paper_id)

            # 空のjson(=まだ検索されたことのない論文)ならば、DeepLを用いて日本語を追加したjsonを返す。
            if len(paper_json)==0:

                paper_json = search_paper.add_ja_title(paper)
                # データベースに追加
                add_title(paper_json)
            
            # リストに追加
            search_list.append(paper_json)
        
        return Response(search_list)
        

# Paper_detailのgetメソッドを用いたDebug用  
contents =  {
        "Paper_ID": "http://arxiv.org/abs/2307.08701v1",
        "Title_En": "AlpaGasus: Training A Better Alpaca with Fewer Data",
        "Content_En": "Large language models~(LLMs) obtain instruction-following capability throughinstruction-finetuning (IFT) on supervised instruction/response data. However,widely used IFT datasets (e.g., Alpaca's 52k data) surprisingly contain manylow-quality instances with incorrect or irrelevant responses, which aremisleading and detrimental to IFT. In this paper, we propose a simple andeffective data selection strategy that automatically identifies and removeslow-quality data using a strong LLM (e.g., ChatGPT). To this end, we introduceAlpaGasus, which is finetuned on only 9k high-quality data filtered from the52k Alpaca data. AlpaGasus significantly outperforms the original Alpaca asevaluated by GPT-4 on multiple test sets and its 13B variant matches $>90\\%$performance of its teacher LLM (i.e., Text-Davinci-003) on test tasks. It alsoprovides 5.7x faster training, reducing the training time for a 7B variant from80 minutes (for Alpaca) to 14 minutes \\footnote{We apply IFT for the samenumber of epochs as Alpaca(7B) but on fewer data, using 4$\\times$NVIDIA A100(80GB) GPUs and following the original Alpaca setting and hyperparameters.}.Overall, AlpaGasus demonstrates a novel data-centric IFT paradigm that can begenerally applied to instruction-tuning data, leading to faster training andbetter instruction-following models. Our project page is available at:\\url{https://lichang-chen.github.io/AlpaGasus/}.",
        "Categories": [
            "Computation and Language"
        ],
        "Authors": [
            "Lichang Chen",
            "Shiyang Li",
            "Jun Yan",
            "Hai Wang",
            "Kalpa Gunaratna",
            "Vikas Yadav",
            "Zheng Tang",
            "Vijay Srinivasan",
            "Tianyi Zhou",
            "Heng Huang",
            "Hongxia Jin"
        ],
        "Pdf_url": "http://arxiv.org/pdf/2307.08701v1",
        "Published": "2023-07-17T17:59:40Z",
        "Title_Ja": "アルパガサス少ないデータでより良いアルパカを育てる"
    }


class Paper_detail(APIView):
    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)
        # return Response(paper_detail.main(contents))
    
    def post(self, request, *args, **kwargs):
        if request.data is None:

            search_paper_json = request.session.get('Paper_detail') 
            print(search_paper_json)
            print("二回目")
        
        else:
            request.session["Paper_detail"] = request.data
            search_paper_json = request.data
            print("一回目")

        # return Response(paper_detail.main(search_json))
        
        # Paper_IDを取得

        paper_id = search_paper_json["Paper_ID"]

        # 既に日本語付き論文があればそのまま取得、なければ空のjson(=まだ検索されたことのない論文)を返す。
        paper_plusJa_json = search_papers(paper_id)

        # 空のjson(=まだ検索されたことのない論文)ならば、DeepLを用いて日本語の概要を追加したjsonを返す。
        if len(paper_plusJa_json)==0:
            paper_plusJa_json = paper_detail.main(search_paper_json)

            # データベースに追加
            add_content_keywords(paper_plusJa_json)
        
        return Response(paper_plusJa_json)


# 推薦モデルの作成
class Paper_recommend(APIView):
    def get(self, request):
        return Response(recommendation())
        # return Response(paper_detail.main(contents))