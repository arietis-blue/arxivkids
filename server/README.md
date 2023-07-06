# Server Side

Djangoを用いて実装
## 事前準備 / Advance preparation
<!-- ### 仮想環境の準備
#### pip
`conda_requirements.txt`に記載のpythonライブラリをinstall.

pipでインストール
````
pip install -r conda_requirements.txt
````

#### conda
`conda_requirements.yaml`を用いてinstall.
````
conda env create -f conda_requirements.yaml 
```` -->

### envファイルの作成
`./App_Folder/`下のディレクトリに.envファイルを作成。

そこにOpenAI APIとDeepL APIのそれぞれのキーを書いておく。
````
OPENAI_API_KEY = ~OpenAI API Key~

DEEPL_API_KEY = ~DeepL API Key~
````

## Djangoのサーバーを起動 / Start Django server
`/server/`フォルダにいることを確認して、以下を実行して起動
````
python manage.py runserver
````

http://127.0.0.1:8000
で接続すればOK（現状はPathがないためエラーが出る。）

### ルーティング/Routing

http://127.0.0.1:8000/api/arxiv/
にアクセスすると、入力したキーワード("search")による検索結果のjsonを返す。
````
# 入出力例
input(jsonのリスト): [{"search"}]

Output(jsonのリスト): [{"ID", "Title_En", "Content_En", "Categories", "authors", "Pdf_url","published", "Title_Ja"}]
````

http://127.0.0.1:8000/api/paper
にアクセスすると、入力したjsonファイルに、DeepLを用いてAbstractの日本語訳と平易な日本語を追加

````
# 入出力例
input(jsonのリスト): [{"ID", "Title_En", "Content_En", "Categories", "authors", "Pdf_url","published", "Title_Ja"}]

Output(jsonのリスト): [{"ID", "Title_En", "Content_En", "Categories", "authors", "Pdf_url","published", "Title_Ja", "Content_Ja", "Content_plain"}]
````
