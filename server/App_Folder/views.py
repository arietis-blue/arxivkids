from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .api_call import search_paper, paper_detail

# Arxiv_Searchのgetメソッドを用いたDebug用 
search = {
    "Search": "LLM cat:cs.CL"
}

# Create your views here.
class Arxiv_Search(APIView):
    def get(self, request):
        # return Response("OK", status=status.HTTP_200_OK)
        return Response(search_paper.main(search["Search"]))
    
    def post(self, request, *args, **kwargs):
        search_word = request.data
        return Response(search_paper.main(search_word['Search']))

# Paper_detailのgetメソッドを用いたDebug用  
contents = {
    "Paper_ID": "http://arxiv.org/abs/2307.02486v1",
    "Title_En": "LongNet: Scaling Transformers to 1,000,000,000 Tokens",
    "Content_En": "Scaling sequence length has become a critical demand in the era of large\nlanguage models. However, existing methods struggle with either computational\ncomplexity or model expressivity, rendering the maximum sequence length\nrestricted. In this work, we introduce LongNet, a Transformer variant that can\nscale sequence length to more than 1 billion tokens, without sacrificing the\nperformance on shorter sequences. Specifically, we propose dilated attention,\nwhich expands the attentive field exponentially as the distance grows. LongNet\nhas significant advantages: 1) it has a linear computation complexity and a\nlogarithm dependency between tokens; 2) it can be served as a distributed\ntrainer for extremely long sequences; 3) its dilated attention is a drop-in\nreplacement for standard attention, which can be seamlessly integrated with the\nexisting Transformer-based optimization. Experiments results demonstrate that\nLongNet yields strong performance on both long-sequence modeling and general\nlanguage tasks. Our work opens up new possibilities for modeling very long\nsequences, e.g., treating a whole corpus or even the entire Internet as a\nsequence.",
    "Categories": [
        "Computation and Language",
        "Machine Learning"
    ],
    "Authors": [
        "Jiayu Ding",
        "Shuming Ma",
        "Li Dong",
        "Xingxing Zhang",
        "Shaohan Huang",
        "Wenhui Wang",
        "Furu Wei"
    ],
    "Pdf_url": "http://arxiv.org/pdf/2307.02486v1",
    "Published": "2023-07-05T17:59:38Z",
    "Title_Ja": "ロングネットトランスフォーマーを1,000,000,000トークンに拡張する"
}

class Paper_detail(APIView):
    def get(self, request):
        # return Response("OK", status=status.HTTP_200_OK)
        return Response(paper_detail.main(contents))
    
    def post(self, request, *args, **kwargs):
        search_json = request.data
        return Response(paper_detail.main(search_json))
    
# {
#     "ID": "http://arxiv.org/abs/2307.02486v1",
#     "Title_En": "LongNet: Scaling Transformers to 1,000,000,000 Tokens",
#     "Content_En": "Scaling sequence length has become a critical demand in the era of large\nlanguage models. However, existing methods struggle with either computational\ncomplexity or model expressivity, rendering the maximum sequence length\nrestricted. In this work, we introduce LongNet, a Transformer variant that can\nscale sequence length to more than 1 billion tokens, without sacrificing the\nperformance on shorter sequences. Specifically, we propose dilated attention,\nwhich expands the attentive field exponentially as the distance grows. LongNet\nhas significant advantages: 1) it has a linear computation complexity and a\nlogarithm dependency between tokens; 2) it can be served as a distributed\ntrainer for extremely long sequences; 3) its dilated attention is a drop-in\nreplacement for standard attention, which can be seamlessly integrated with the\nexisting Transformer-based optimization. Experiments results demonstrate that\nLongNet yields strong performance on both long-sequence modeling and general\nlanguage tasks. Our work opens up new possibilities for modeling very long\nsequences, e.g., treating a whole corpus or even the entire Internet as a\nsequence.",
#     "Categories": [
#         "Computation and Language",
#         "Machine Learning"
#     ],
#     "authors": [
#         "Jiayu Ding",
#         "Shuming Ma",
#         "Li Dong",
#         "Xingxing Zhang",
#         "Shaohan Huang",
#         "Wenhui Wang",
#         "Furu Wei"
#     ],
#     "Pdf_url": "http://arxiv.org/pdf/2307.02486v1",
#     "published": "2023-07-05T17:59:38Z",
#     "Title_Ja": "ロングネットトランスフォーマーを1,000,000,000トークンに拡張する",
#     "Content_Ja": "シーケンスの長さをスケーリングすることは、大規模言語モデルの時代において重要な要求となっている。\n重要な要求となっている。しかし、既存の方法は、計算の複雑さとモデルの表現力のどちらか\n計算の複雑さとモデルの表現力のどちらにも苦戦しており、最大配列長\nを制限している。本研究では、Transformerの変種であるLongNetを紹介する。\nより短いシーケンスの性能を犠牲にすることなく、シーケンスの長さを10億トークン以上に拡張できる\nを導入する。具体的には、拡張注意（dilated attention）を提案する、\nこれは距離が長くなるにつれて、注意フィールドを指数関数的に拡大する。ロングネット\nには大きな利点がある：1)計算の複雑さは線形で、トークン間の依存関係は対数である。\nトークン間の依存性が対数である。\n3）その拡張された注意は、標準的な注意に取って代わることができる。\n標準的なアテンションとシームレスに統合できる。\n既存のTransformerベースの最適化とシームレスに統合できる。実験の結果\nLongNetは、長シーケンスモデリングと一般的な言語タスクの両方において強力な性能を発揮する。\n言語タスクの両方で強力な性能を発揮することが実証された。我々の研究は、非常に長いシーケンスのモデリングに新たな可能性を開く。\n例えば、コーパス全体やインターネット全体をシーケンスのように扱うことができる。\nシーケンスとして扱うことができる。",
#     "Content_plain": "シーケンスの長さをスケーリングすることは、大規模言語モデルの時代において重要な要求となっている。既存の方法は、計算の複雑さとモデルの表現力のどちらかに苦戦しており、最大配列長を制限している。本研究では、Transformerの変種であるLongNetを紹介する。LongNetは、シーケンスの長さを10億トークン以上に拡張できる方法を提案している。具体的には、拡張注意を導入し、距離が長くなるにつれて注意フィールドを指数関数的に拡大する。LongNetは、計算の複雑さが線形であり、トークン間の依存関係が対数であるという利点があり、既存のTransformerベースの最適化とシームレスに統合できる。実験の結果、LongNetは長シーケンスモデリングと一般的な言語タスクの両方で強力な性能を発揮することが実証された。この研究は、非常に長いシーケンスのモデリングに新たな可能性を開くことが示されており、例えば、コーパス全体やインターネット全体をシーケンスとして扱うことができるようになる可能性がある。"
# }