# arXiv Friends
arXivの英語論文を専門外の人にもわかりやすく日本語で。


## API Keyの設定
`./server/App_Folder/`下のディレクトリに.envファイルを作成。

そこにOpenAI APIとDeepL APIのそれぞれのキーを書いておく。こちらは各自で取得。
````
OPENAI_API_KEY = ~OpenAI API Key~

DEEPL_API_KEY = ~DeepL API Key~
````

## プロジェクトの使用の立ち上げ方
### Step.1 Server　
`./server`フォルダに移動する。

まず、1回目のみ以下を実行する。
````
python manage.py migrate
````

次に以下を実行する。
````
python manage.py runserver
````
その状態で、
http://localhost:8000
を起動する。


### Step.2 Client　
Node.jsをDownload(https://nodejs.org/ja/download)

次に./clientというフォルダーの中で
````
npm install
npm run dev
````

その状態で、
http://localhost:5173
を起動する。