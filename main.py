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
tit = []
new_title = []    #새 제목만 가져오는 리스트
tit_new = []
tit_re_list = []    
tit_modi_list = []

divs = soup.select('div.board-text > a')
tit_res = soup.select('p.info')    #게시글 등록 날짜
tit_modis = soup.select('p.info')    #게시글 수정된 날짜

for div in divs:
    title = ''.join(div.text.split())
    title_list.append(title.replace("신규게시글", '').replace("Attachment", ''))
    link_list.append(div.get('href'))

for i in range(5):      #추출된 제목 리스트에서 5개만 tit리스트에 넣습니다.
    tit.append(title_list[i])
    tit_new.append(title_list[i])
    
for tit_modi in tit_modis: 
    tit_modi_list.append(tit_modi.text.split()[7]) #수정된 날짜
    tit_re_list.append(tit_modi.text.split()[4]) #등록된 날짜

tit_new = tit[:]    #저장용 제목 리스트를 추출된 제목 리스트로 초기화 합니다. =로 단순 대입하면 주소값을 복제 하기에 tit이 바뀌면 tit_sa도 바뀜
tit_new[3] = '가가가가가가'   #의도적으로 tit_new의 3번째 요소를 변경합니다. / 3번 째 requests.get에서 title의 목록이 변경되었다는 것을 의미

for check in tit_new:
    if check not in tit:     #tit_new와 tit를 비교하여 tit의 새로운 요소를 new_title에 추가합니다.
        new_title.append(check)
        tit[:]    #새로운 요소를 추가한 후 저장리스트를 다시 저장합니다.
    else:    #tit_new가 tit와 같은 경우
        if tit_modi_list == tit_re_list:    #수정된 날짜가 등록된 날짜와 같은 경우
            break
        else:    #수정된 날짜가 등록된 날짜와 다른 경우
            new_title.append(check)
    
print(new_title)