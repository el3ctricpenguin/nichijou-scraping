import requests, json, os, shutil
from bs4 import BeautifulSoup

def download_image(_url,_title):
    os.mkdir(_title)
    print('mkdir: '+_title)

    _url+='json'

    _response = requests.get(_url)

    img_list = _response.json()

    for i in range(len(img_list)):
        _response = requests.get(master_url+img_list[i], stream = True)
        if _response.status_code == 200:
            filename = _title + '_' + str(i+1)+'.jpg'
            with open(_title + '/' + filename,'wb') as f:
                shutil.copyfileobj(_response.raw,f)
        else:
            print('couldn\'t save the image... img no.'+ str(i+1))

def zenkakuToHankaku(text):
    return text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

master_url='https://web-ace.jp'
url='https://web-ace.jp/youngaceup/contents/1000069/episode/'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

container = soup.find('div', attrs={"id" : "read"})

cards = container.find_all("li", attrs={"class": ["table-view-cell", "media"]})

for card in cards:
    title = zenkakuToHankaku(card.find('h3').text)
    link = master_url + card.find("a").get('href')
    download_image(link,title)
