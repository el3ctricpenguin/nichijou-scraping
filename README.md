# nichijou-scraping
某サイトで１週間だけ全巻無料公開されていた某漫画の全エピソードをダウンロードするためのスクリプト。  
現在は無料期間が終わってしまったため使えないが、他の漫画にも転用できそう(urlの値を変える)。

## 必要なもの
- Python3
- Requests, BeautifulSoup (Pythonパッケージ)

## 導入方法
Python3を何とかしてインストール(pipもインストールされるはず)  
各OSごとのインストール方法 (https://www.python.jp/install/install.html)

pipを使ってrequests, beautifulsoup4をインストール (既にインストールしていなければ)  
`pip3 install requests`  
`pip3 install beautifulsoup4`

コードを実行 (ファイルがあるディレクトリにそのまま新しいディレクトリ(日常の〇〇)が作られていきます)  
`python3 download-all-nichijou-eps.py`
