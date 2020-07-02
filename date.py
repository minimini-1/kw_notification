import requests
from bs4 import BeautifulSoup

url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

rgdate_list = []
mddate_list = []

rgdates = soup.select('p.info')
mddates = soup.select('p.info')

for rgdate in rgdates:
    rgdate_list.append(rgdate.text.split()[4])
for mddate in mddates:
    mddate_list.append(mddate.text.split()[7])

print(rgdate_list)
print(mddate_list)
