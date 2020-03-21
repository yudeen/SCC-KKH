print('hiiii')


a=3
b=a
a=a+1
print(a,b+1)

name = 'bbb'
num = 12
is_number = not True
print(name, num, is_number)

a_list = []
a_list.append(5)
a_list.append('hi')
print(a_list)
a_list.append([2,3])
print(a_list)
print(a_list[2])

a_dict={}
kwanghan = {'name':'광한', 'ki': 175}
print(kwanghan['ki'])
kwanghan['weight']=49
print(kwanghan['weight'])

def f(x):
    return 2*x+3
print(f(5))


def sum_all(a,b,c):
	return a+b+c

def mul(a,b):
	return a*b

result = sum_all(1,2,3) + mul(10,10)

print(result)


a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def check_mail(s):
    if s.find('@') == -1:
        return False
    else :
        return True
print(check_mail(a))


a = 'spartacodingclub@gmail.com'
def find_mail(s):
    return s.split('@')[1].split('.')[0]

print(find_mail(a))


#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
    empty_basket = {}
    basket = {'사과' : 0,'감' : 0,'배' : 0,'포도' : 0,'딸기' : 0,'수박' : 0}
    for fruit in a_list:
        basket[fruit] = basket[fruit]+1

        if fruit in empty_basket:
            empty_basket[fruit] = empty_basket[fruit] + 1
        else :
            empty_basket[fruit] = 1

    return print(basket)

import requests # requests 라이브러리 설치 필요 import는 api를 불러주는거 ajax 같은거

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
gu_list = rjson['RealtimeCityAir']['row']
for gu in gu_list:
    print (gu['MSRSTE_NM'],gu['IDEX_MVL'])
