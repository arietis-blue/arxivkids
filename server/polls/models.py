# モデル読込
from django.db import models

# モデルクラスを作成
class Papers(models.Model):
    
    ID           = models.CharField(max_length=100)             #論文ID                   arxiv
    Title_En     = models.TextField(blank=True, null=True)      #英語タイトル               arxiv
    Title_Ja     = models.EmailField(max_length=100)            #日本語タイトル             deepl
    Content_En   = models.TextField()                           #abstract                arxiv
    Content_Ja   = models.TextField()                           #abstract                deepl
    Search_num   = models.IntegerField(blank=True, null=True)   #検索回数   


class Keywords(models.Model):

    ID           = models.CharField(max_length=100)             #論文ID   arxiv
    Keyword      = models.TextField()                              
    Description  = models.TextField()   