# モデル読込
from django.db import models

# モデルクラスを作成
class Papers(models.Model):
    
    Paper_ID     = models.CharField(max_length=1000)             #論文ID                   arxiv
    Title_En     = models.TextField()      #英語タイトル               arxiv
    Title_Ja     = models.TextField()            #日本語タイトル             deepl
    Content_En   = models.TextField(null = True)                           #abstract                arxiv
    Content_Ja   = models.TextField(null = True)                           #abstract                deepl
    Search_num   = models.IntegerField(null=True)   #検索回数   


class Keywords(models.Model):

    Paper_ID     = models.CharField(max_length=1000)             #論文ID   arxiv
    Keyword      = models.TextField()                              
    Description  = models.TextField()   


class Profile(models.Model):

    User_ID     = models.IntegerField()             #ユーザーID
    Name        = models.CharField(max_length=100)                  #ニックネーム  
    Pass        = models.CharField(max_length=100)                               #パスワード


class Reads(models.Model):

    Paper_ID     = models.CharField(max_length=1000)             #論文ID
    Reader_ID    = models.IntegerField(null=True)               #読んだ人のID               
    Date         = models.DateTimeField()                       #日時