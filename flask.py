from flask import Flask, request, jsonify
import sys
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)

def res():
    url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    title_list = []
    link_list = []
    link_lists = []
    title_lists = []
    titles = soup.select('div.board-text > a')
    links = soup.select('div.board-text > a')
    
    for title in titles:
        title = title.text
        title = ''.join(title.split())
        title_list.append(title)
    
    for link in links:
        link = link.get('href')
        link_list.append(link)
        
    for i in range(10):
        title_lists.append(title_list[i].replace("신규게시글", "").replace("Attachment",""))
        link_lists.append("https://www.kw.ac.kr" + link_list[i])
        i = i+1
    return ('\n'.join(title_lists))
        
@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if content == u"안녕":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": res()
                        }
                    }
                ]
            }
        }
    else :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "아직 공부하고있습니다."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0')