import requests
from bs4 import BeautifulSoup
import datetime
import time
url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

saved_title_list = []

while True:
    title_list = []
    link_list = []
    register_date_list = []
    modified_date_list = []
    new_index = []
    new_title = []
    new_link = []

    req = requests.get(url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    register_dates = soup.select('p.info')
    modified_dates = soup.select('p.info')
    divs = soup.select('div.board-text > a')

    for div in divs:            #제목과 링크를 얻기 위한 반복문
        title = ''.join(div.text.split())
        title_list.append(title.replace("신규게시글", '').replace("Attachment", ''))
        link_list.append(div.get('href'))

    for register_date in register_dates:
        register_date_list.append(register_date.text.split()[4])
    for modified_date in modified_dates:
        modified_date_list.append(modified_date.text.split()[7])

    if saved_title_list != title_list:  #기존에 저장된 데이터와 비교
        for check in title_list:
            if check not in saved_title_list:
                new_index.append(title_list.index(check))
        for i in range(len(register_date_list)):
            if register_date_list[i] != modified_date_list[i] and modified_date_list[i] == datetime.date.today(): # 수정된 날이 다르고 현재 날짜와 다름
                new_index.append(modified_date_list.index(modified_date_list[i]))
    saved_title_list = title_list[:]

    for index in new_index:     #인덱스를 통한 새로운 제목과 링크를 추가
        new_title.append(title_list[index])
        new_link.append(link_list[index])

    time.sleep(60 * 60)     #한 시간 마다 반복문 실행