import re
import requests

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'

response = requests.get(url)
text = response.content.decode('utf-8')     # euc-kr
print(text)

# codes = re.findall(r'[0-9]+', text)
# areas = re.findall(f'[가-힣]+', text)


# for c, a in zip(codes, areas):
#     print(c, a)


# items = re.findall(r'[0-9]+[가-힣]+', text)
# print(items)

items = re.findall(r'{"code":"([0-9]+)","value":"([가-힣]+)"}', text)
# items = re.findall(r'{"code":"[0-9]+","value":"[가-힣]+"}', text)
# 괄호로 묶어주면 괄호끼리 묶어서 호출 // 괄호 없으면 패턴 째로 호출
# ex) [('11', '서울특별시'), ('26', '부산광역시'), ... // ['{"code":"11","value":"서울특별시"}', '{"code":"26","value":"부산광역시"}', ....
print(items)
