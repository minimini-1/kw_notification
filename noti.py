import requests
from bs4 import BeautifulSoup

url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
html = requests.get(url, headers=header)
soup = BeautifulSoup(html.text, 'html.parser')

title_list = []
link_list = []
        
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
    print(title_list[i])
    print("https://www.kw.ac.kr" + link_list[i])
    i = i+1