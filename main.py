import requests
from bs4 import BeautifulSoup

url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

saved_title_list = []
title_list = []
link_list = []
register_date_list = []
modified_date_list = []

while True:
    new_title = []

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
                new_title.append(check)
        saved_title_list = title_list[:]
