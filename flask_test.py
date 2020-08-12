from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
html = requests.get(url, headers=header)
soup = BeautifulSoup(html.text, 'html.parser')
title_list = []
link_list = []
link_lists = []
title_lists = []
titles = soup.select('div.board-text > a')
links = soup.select('div.board-text > a')


@app.route('/')
def index():
    return "hi~"


def title(j):
    for title in titles:
        title = title.text
        title = ''.join(title.split())
        title_list.append(title)

    for i in range(10):
        title_lists.append(title_list[i].replace("신규게시글", "").replace("Attachment", ""))
        i = i + 1

    return (title_lists[j])


def link(k):
    for link in links:
        link = link.get('href')
        link_list.append(link)

    for i in range(10):
        link_lists.append("https://www.kw.ac.kr" + link_list[i])
        i = i + 1
    return (link_lists[k])
def makejs():
    item_list = []
    for t in range(5):
        item_set = {"title": "", "buttons": ""}
        buttons_list = []
        buttons_set = {"action": "webLink" , "label": "링크열기", "webLinkUrl": ""}
        buttons_set["webLinkUrl"] = link(t)
        buttons_list.append(buttons_set)
        item_set["title"] = title(t)
        item_set["buttons"] = buttons_list
        item_list.append(item_set)
    return item_list


@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    dataSend = {
        "version": "2.0",
        "template": {
            "quickReplies": [
                {
                    "label": "더 보기",
                    "action": "message"

                }
            ],
            "outputs": [

                {
                    "carousel": {
                        "type": "basicCard",
                        "items":

                                makejs()


                    }
                }
            ]
        }
    }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', prot='40215')

