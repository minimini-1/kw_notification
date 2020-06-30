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

#titles = soup.select('div.board-text > a')
#links = soup.select('div.board-text > a')
register_dates = soup.select('p.info')
modified_dates = soup.select('p.info')
divs = soup.select('div.board-text > a')

for div in divs:
    i = 0
    title = ''.join(div.text.split())
    title_list.append(title)
    link_list.append(div.get('href'))
    print(title_list[i] + link_list[i])
    i += 1
'''   
for title in titles:
    title = title.text
    title = ''.join(title.split())
    title_list.append(title)
for link in links:
    link = link.get('href')
    link_list.append(link)
'''  
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
print("신규등록")
for i in new_register_index:
    new_title.append(title_list[i])
    #print(title_list[i])
print("신규수정")
for i in new_modified_index:
    if title_list[i] in new_title:
        continue
    #print(title_list[i])