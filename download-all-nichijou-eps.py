import requests, json, os, shutil
from bs4 import BeautifulSoup

#このサイトはリンクを絶対パスで書いてるので (ドメイン名) + (hrefの文字列) で実際のURLになる
master_url='https://web-ace.jp'
url='https://web-ace.jp/youngaceup/contents/1000069/episode/'

#漫画ページのURL, タイトル を受け取る
#タイトル名のフォルダをつくる
#そのページの漫画画像ファイルをフォルダ内に全てダウンロードする
def download_image(_url,_title):
    #タイトル名でフォルダを作る
    os.mkdir(_title)
    print('mkdir: '+_title)

    #漫画ページのURLに /jsonをつけると画像のURLが書かれたjsonファイルが出てくる
    _url+='json'
    _response = requests.get(_url)
    #jsonとして読み込む
    img_list = _response.json()

    #JSON内の画像ファイルを順番にダウンロードしていく
    for i in range(len(img_list)):
        _response = requests.get(master_url+img_list[i], stream = True)
        if _response.status_code == 200:
            #(タイトル名)+(番号).jpg
            filename = _title + '_' + str(i+1)+'.jpg'
            with open(_title + '/' + filename,'wb') as f:
                shutil.copyfileobj(_response.raw,f)
        else:
            print('couldn\'t save the image... img no.'+ str(i+1))

def zenkakuToHankaku(text):
    return text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

#エピソード一覧のページから各エピソードへのリンクとエピソード名を取得する
#各カードごとにタイトルの数字を全角→半角変換した後、リンクとタイトルをdownload_image()に投げる
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

container = soup.find('div', attrs={"id" : "read"})

cards = container.find_all("li", attrs={"class": ["table-view-cell", "media"]})

for card in cards:
    title = zenkakuToHankaku(card.find('h3').text)
    link = master_url + card.find("a").get('href')
    download_image(link,title)
