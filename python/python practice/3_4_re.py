import re
import requests


#도서관 예제
# url = 'http://211.251.214.176:8800/index.php?room_no=2'
# response = requests.get(url)
# print(response.text)


# pattern = r'<font style="color:green;font-size:13pt;font-family:Arial"><b>([0-9]+)</b>'
# empty = re.findall(pattern, response.text)
# print(empty)
# print(len(empty))


# print([int(n) for n in empty]

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=184'

response = requests.get(url)
# print(response.text)

# print(re.findall(r'<province>(.+)</province>', response.text))
# print(re.findall(r'<city>(.+)</city>', response.text))


locations = re.findall(r'<location wl_ver="3">(.+?)</location>',\
                       response.text, re.DOTALL)

# print(locations)
# print(len(locations))

f = open('./weather.csv', 'w', encoding='utf-8')
for loc in locations:
    # prov = re.findall(r'<province>(.+)</province>', loc)
    # city = re.findall(r'<city>(.+)</city>', loc)
    # print(prov[0], city[0])

    # prov_city = re.findall(r'<province>(.+)</province>.+<city>(.+)</city>', loc, re.DOTALL)

    pattern = r'<province>(.+)</province>.+<city>(.+)</city>'
    prov_city = re.findall(pattern, loc, re.DOTALL)
    # print(prov_city, prov_city)
    # print(prov_city[0][0], prov_city[0][1])
    # print(*prov_city[0])


    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    # print(len(data))

    for datum in data:
        mode = re.findall(r'<mode>(.+)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        wf = re.findall(r'<wf>(.+)</wf>', datum)
        tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
        rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)

        # print(*prov_city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0])
        # print(*prov_city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0],
        #       file=f, sep=',')

        # base = '{},{},{},{},{},{},{},{}\n'
        f.write('{},{},{},{},{},{},{},{}\n'.format(*prov_city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0]))

f.close()

