import requests # requests 라이브러리 설치 필요 import는 api를 불러주는거 ajax 같은거

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
gu_list = rjson['RealtimeCityAir']['row']
for gu in gu_list:
    print (gu['MSRSTE_NM'],gu['IDEX_MVL'])
