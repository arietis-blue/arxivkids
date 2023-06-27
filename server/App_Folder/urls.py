from django.urls import path
from App_Folder.views import Arxiv_Search

urlpatterns = [
    path('arxivkids/', Arxiv_Search.as_view(), name='index'),
    # path('diaries/', DiaryView.as_view()),
    # path('diaries/<int:diary_id>/', DiaryByIDView.as_view()),
    # path('diaries/CommentView/<int:diary_id>', DiaryCommentView.as_view()),
]