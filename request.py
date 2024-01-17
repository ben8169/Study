import requests

url = "http://127.0.0.1:8000/api/formula/1"

# GET 요청 보내기
response = requests.get(url)

if response.status_code == 200:
    # JSON 데이터 추출
    data = response.json()

    # 데이터 확인
    print(data)
else:
    print(f"{url}에 GET 요청에 실패했습니다. 응답 코드:", response.status_code)
