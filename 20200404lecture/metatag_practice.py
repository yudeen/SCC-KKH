import requests
from bs4 import BeautifulSoup

url = 'https://platum.kr/archives/120958'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.

# beautiful soup로 태그 정보를 가져와서
og_image = soup.select_one('meta[property="og:image"]')  
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

#dictionary로 만들고
url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']

#dictionary 정보를 프린트함
print(url_image)
print(url_title)
print(url_description)
