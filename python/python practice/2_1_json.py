import json
import requests

a = {"ip": "8.8.8.8"}
print(a)

b = json.dumps(a)
print(b, type(b))

c = json.loads(b)
print(c, type(c))

d = '''{
   "time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''

e = json.loads(d)
print(e)
print(e['time'], e['milliseconds_since_epoch'], e['date'])
print(e.values())

for k in e:
    print(e[k])

# print('-' * 30)
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)
print(response)
print(response.text)    # str
print(response.content) # bytes

text = response.content.decode('utf-8')
print(text)

items = json.loads(text)
print(type(items))

for item in items:
    # print(item['code'], item['value'])

    for k in item:
        print(item[k], end=' ')
    print()


    
