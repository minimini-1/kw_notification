from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kwnoti-fefb3.firebaseio.com/'
})
app = Flask(__name__)


def getdb(utr):
    if utr == "일반-학사":
        ref1 = db.reference("제목/일반-학사")
        ref2 = db.reference("링크/일반-학사")
        title_list = ref1.get()
        link_list = ref2.get()
    elif utr == "학생-봉사":
        ref1 = db.reference("제목/학생-봉사")
        ref2 = db.reference("링크/학생-봉사")
        title_list = ref1.get()
        link_list = ref2.get()
    elif utr == "등록-장학":
        ref1 = db.reference("제목/등록-장학")
        ref2 = db.reference("링크/등록-장학")
        title_list = ref1.get()
        link_list = ref2.get()
    elif utr == "입학-시설":
        ref1 = db.reference("제목/입학-시설")
        ref2 = db.reference("링크/입학-시설")
        title_list = ref1.get()
        link_list = ref2.get()
    elif utr == "병무-외부":
        ref1 = db.reference("제목/병무-외부")
        ref2 = db.reference("링크/병무-외부")
        title_list = ref1.get()
        link_list = ref2.get()
    elif utr == "국제교류-국제학생":
        ref1 = db.reference("제목/국제교류-국제학생")
        ref2 = db.reference("링크/국제교류-국제학생")
        title_list = ref1.get()
        link_list = ref2.get()
    elif utr == "전체":
        ref1 = db.reference("제목/전체")
        ref2 = db.reference("링크/전체")
        title_list = ref1.get()
        link_list = ref2.get()
    return title_list, link_list


def makejs(title_list, link_list):
    item_list = []
    for t in range(len(title_list)):
        item_set = {"title": "", "buttons": ""}
        buttons_list = []
        buttons_set = {"action": "webLink" , "label": "링크열기", "webLinkUrl": ""}
        buttons_set["webLinkUrl"] = link_list[t]
        buttons_list.append(buttons_set)
        item_set["title"] = title_list[t]
        item_set["buttons"] = buttons_list
        item_list.append(item_set)
    return item_list


@app.route('/')
def index():
    return "hi~"


@app.route('/message', methods=['POST'])
def Message():
    utr = request.get_json()
    utr = utr["userRequest"]
    utr = utr["utterance"]
    title_list, link_list = getdb(utr)
    if title_list[0] != 0:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items":
                                makejs(title_list, link_list)
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "최근 등록된 게시물이 없습니다."
                        }
                    }
                ]
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', prot='40215')

