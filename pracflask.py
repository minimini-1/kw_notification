import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def makeurl(utr):
    title_list = []
    link_list = []
    ref1 = db.reference("제목")
    ref2 = db.reference("링크")

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    if utr == "일반-학사":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=0&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=1&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        ref1.update({"일반-학사": title_list})
        ref2.update({"일반-학사": link_list})
    elif utr == "병무-외부":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=7&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=8&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        ref1.update({"병무-외부": title_list})
        ref2.update({"병무-외부": link_list})
    elif utr == "등록-장학":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=4&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        ref1.update({"등록-장학": title_list})
        ref2.update({"등록-장학": link_list})
    elif utr == "입학-시설":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=5&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=6&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        ref1.update({"입학-시설": title_list})
        ref2.update({"입학-시설": link_list})
    elif utr == "전체":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        ref1.update({"전체": title_list})
        ref2.update({"전체": link_list})
    elif utr == "학생-봉사":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=2&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=3&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        ref1.update({"학생-봉사": title_list})
        ref2.update({"학생-봉사": link_list})
    elif utr == "국제교류-국제학생":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=9&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=10&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        ref1.update({"국제교류-국제학생": title_list})
        ref2.update({"국제교류-국제학생": link_list})



def maketitle(parsing, title_list):
    for title in parsing:
        if "신규게시글" in title.text:
            title = title.text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))


def makelink(parsing, link_list):
    for link in parsing:
        if "신규게시글" in link.text:
            link = link.get('href')
            link_list.append("https://www.kw.ac.kr" + link)


#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://kwnoti-fefb3.firebaseio.com/'
})

categorize = ["일반-학사", "병무-외부", "등록-장학", "입학-시설", "학생-봉사", "전체", "국제교류-국제학생"]

for utr in categorize:
    makeurl(utr)
