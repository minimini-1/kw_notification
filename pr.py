import requests
from bs4 import BeautifulSoup

title_list = []
link_list = []


def makeurl(con):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    if con == "일반/학사":
        index_list = []
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=0&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=1&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        for idx in range(len(content1)):
            if "신규게시글" in content1[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content1[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content1[idx].get('href'))
        index_list = []
        for idx in range(len(content2)):
            if "신규게시글" in content2[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content2[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content2[idx].get('href'))
    elif con == "학생/봉사":
        index_list = []
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=2&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=3&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        for idx in range(len(content1)):
            if "신규게시글" in content1[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content1[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content1[idx].get('href'))
        index_list = []
        for idx in range(len(content2)):
            if "신규게시글" in content2[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content2[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content2[idx].get('href'))
    elif con == "입학/시설":
        index_list = []
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=5&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=6&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        for idx in range(len(content1)):
            if "신규게시글" in content1[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content1[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content1[idx].get('href'))
        index_list = []
        for idx in range(len(content2)):
            if "신규게시글" in content2[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content2[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content2[idx].get('href'))
    elif con == "병무/외부":
        index_list = []
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=7&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=8&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        for idx in range(len(content1)):
            if "신규게시글" in content1[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content1[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content1[idx].get('href'))
        index_list = []
        for idx in range(len(content2)):
            if "신규게시글" in content2[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content2[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content2[idx].get('href'))
    elif con == "국제교류/국제학생":
        index_list = []
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=9&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=10&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        for idx in range(len(content1)):
            if "신규게시글" in content1[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content1[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content1[idx].get('href'))
        index_list = []
        for idx in range(len(content2)):
            if "신규게시글" in content2[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content2[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content2[idx].get('href'))
    else:
        index_list = []
        url = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=4&mode=list&searchKey=1&searchVal="
        html = requests.get(url, headers=header)
        soup = BeautifulSoup(html.text, 'html.parser')
        content = soup.select('div.board-text > a')
        for idx in range(len(content)):
            if "신규게시글" in content[idx].text:
                index_list.append(idx)
        for idx in index_list:
            title = content[idx].text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))
            link_list.append("https://www.kw.ac.kr" + content[idx].get('href'))


def makejs():
    item_list = []
    for t in range(len(title_list)):
        item_set = {"title": "", "buttons": ""}
        buttons_list = []
        buttons_set = {"action": "webLink", "label": "링크열기", "webLinkUrl": ""}
        buttons_set["webLinkUrl"] = link_list[t]
        buttons_list.append(buttons_set)
        item_set["title"] = title_list[t]
        item_set["buttons"] = buttons_list
        item_list.append(item_set)
    return item_list
makeurl("일반/학사")
print(makejs())