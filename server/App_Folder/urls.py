from django.urls import path
from App_Folder.views import Arxiv_Search, Paper_detail

urlpatterns = [
    # 入力したキーワードによる検索結果を表示
    # input(json): {"search"}
    # Output(json): {"ID", "Title_En", "Content_En", "Categories", "authors", "Pdf_url","published", "Title_Ja"}
    path('arxiv/', Arxiv_Search.as_view(), name='index'),

    # 論文を押したときにAbstractの日本語訳と平易な日本語を追加("Content_Ja", "Content_plain")
    # input(json): {"ID", "Title_En", "Content_En", "Categories", "authors", "Pdf_url","published", "Title_Ja"}
    # Output(json): {"ID", "Title_En", "Content_En", "Categories", "authors", "Pdf_url","published", "Title_Ja", "Content_Ja", "Content_plain"}
    path('paper/', Paper_detail.as_view(), name='index'),

    # path('diaries/', DiaryView.as_view()),
    # path('diaries/<int:diary_id>/', DiaryByIDView.as_view()),
    # path('diaries/CommentView/<int:diary_id>', DiaryCommentView.as_view()),
]