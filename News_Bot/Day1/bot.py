import requests

# 디스코드 웹훅 URL
WEBHOOK_URL = "uwu"

# 디스코드로 보낼 메시지
message = {
    "content": "1일차 테스트: Hello World!"
}

response = requests.post(WEBHOOK_URL, json=message)

# 잘 갔는지 확인하기
if response.status_code == 204:
    print("메시지 전송 성공 디스코드를 확인해보세요.")
else:
    print(f"전송 실패 상태 코드: {response.status_code}")