import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

ranks = soup.select('#old_content > table > tbody > tr > td.range.ac')
titles = soup.select('#old_content > table > tbody > tr .title > div > a')
points = soup.select('#old_content > table > tbody > tr > td.point')


# F12 > 해당영역에서 Copy_Selector > nth-child(2)를 제거하면 위에랑 비슷해짐
# tt = soup.select('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')


# for title in titles :
#     print(title.text)
#
# for point in points :
#     print(point.text)


for item in zip (titles, points, ranks):
    print(item[0].text, item[1].text, item[2].text)


