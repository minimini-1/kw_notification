import requests
from bs4 import BeautifulSoup
import datetime
url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

title_list = []
link_list = []
register_date_list = []
modified_date_list = []
new_register_index = []
new_modified_index = []

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

index = 0
for check in register_date_list:
    if check == str(datetime.date.today()):
        new_register_index.append(index)
    index += 1
index = 0
for check in modified_date_list:
    if check == str(datetime.date.today()):
        new_modified_index.append(index)
    index += 1

new_title = []
register_title = []

for i in new_register_index:            #금일 새로 등록된 제목 리스트를 만드는 반복문
    new_title.append(title_list[i])
for i in new_modified_index:
    if title_list[i] in new_title:          #금일 수정된 제목 리스트를 만드는 반복문
        continue
    register_title.append(title_list[i])
today_title = new_title + register_title    #금일 새롭게 업데이트 된 제목들의 리스트(이거 가지고 비교하면 될거같은 생각)
