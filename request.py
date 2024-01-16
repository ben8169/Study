import requests

url = f"http://127.0.0.1:8000/api/formula/1"
answer = 3754+8452  # 사용자의 답
payload = {"answer": answer}

response = requests.post(url, data=payload)
# response = requests.get(url)

# print(response)
print(response.text)