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

divs = soup.select('div.board-text > a')

for div in divs:
    title = ''.join(div.text.split())
    title_list.append(title.replace("신규게시글", '').replace("Attachment", ''))
    link_list.append(div.get('href'))
    
tit = []
new_title = []
tit_sa = []
tit_re = []
tit_sa_modi = []

for i in range(5):      #추출된 제목 리스트에서 5개만 tit리스트에 넣습니다.
    tit.append(title_list[i])
    tit_sa.append(title_list[i])

tit_sa = tit[:]    #저장용 제목 리스트를 추출된 제목 리스트로 초기화 합니다. =로 단순 대입하면 주소값을 복제 하기에 tit이 바뀌면 tit_sa도 바뀜
#s = 0
#for i in tit:
#if s == 3:
tit[3] = '가가가가가가'   #의도적으로 tit의 3번째 요소를 변경합니다. / 3번 째 requests.get에서 title의 목록이 변경되었다는 것을 의미
for check in tit:
    if check not in tit_sa:     #tit와 tit_sa를 비교하여 tit의 새로운 요소를 new_title에 추가합니다.
        new_title.append(check)
        tit_sa = tit    #새로운 요소를 추가한 후 저장리스트를 다시 저장합니다.
        '''
        수정된 날짜를 확인하여 새로운 제목리스트에 추가하는 것 같은데 구현 방법이 잘 이해가 안되고 생각이 안나서 주석처리함
        
        else:
            j = 0
            for i in title_list:
                if i in tit_sa[s] and i in tit[s]:
                    tit_sa_modi.append(i.text.split()[7]) #수정된 날짜
                    tit_re.append(i.text.split()[4]) #등록된 날짜
                    if tit_sa_modi != tit_re:
                        new_title.append(tit_sa)
                j += 1
         '''
    #s += 1
    
print(new_title)

