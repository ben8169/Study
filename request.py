import requests

response_start = requests.get(f"http://srv1.kitriwhs.kr:23671/api/start")

if response_start.status_code == 200:
    print(response_start.json())
    # 세션 생성에 성공했으므로 세션 ID를 저장
    session_id = response_start.cookies.get("session")
    print("세션 생성에 성공했습니다.")
    print("세션 ID:", session_id)

else:
    print("세션 생성에 실패했습니다.")


# 반복 횟수 설정
num_iterations = 1



for i in range(1, num_iterations+1):
    #세션 id 유지
    session = requests.Session()
    session.cookies.set("session", session_id)
    
    url = f"http://srv1.kitriwhs.kr:23671/api/formula/{i}"

    # GET 요청 보내기
    response = requests.get(url)

    if response.status_code == 200:
        # JSON 데이터 추출
        data = response.json()
        print(data)

        # a와 b 값을 추출하여 계산
        a = data.get("a")
        b = data.get("b")
        answer = a + b

        # POST 요청 데이터 설정
        post_data = {"answer": answer}

        # POST 요청 보내기
        post_response = requests.post(url, data=post_data)

        if post_response.status_code == 200:
            print(f"{url}에 POST 요청이 성공적으로 보내졌. 응답 코드:", post_response.status_code)
        else:
            print(f"{url}에 POST 요청에 실패했습니다. 응답 코드:", post_response.status_code)
    else:
        print(f"{url}에 GET 요청에 실패했습니다. 응답 코드:", response.status_code)

