import os
import requests
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()
api_key = os.getenv("AGENT_API_KEY")
api_url = os.getenv("AGENT_API_URL")

print(f"API URL: {api_url}")
print(f"API Key: {api_key[:20] if api_key else 'None'}...")

# 간단한 요청 테스트
try:
    response = requests.post(
        api_url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"message": "test", "session_id": "test123"},
        timeout=10,
    )

    print(f"상태 코드: {response.status_code}")
    print(f"응답 내용: {response.text}")

    if response.status_code == 200:
        print("✅ API 연결 성공!")
    else:
        print("❌ API 에러 발생")

except Exception as e:
    print(f"❌ 연결 실패: {e}")
