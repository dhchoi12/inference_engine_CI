import requests
import json
import os

# API 엔드포인트 설정 (Azure VM 퍼블릭 IP 사용)
API_URL = os.getenv("INFERENCE_API_URL", "http://localhost:5000/inference")

# 테스트 데이터
test_data = {
    "text": "Hello from Test"
}

# 테스트 실행
test_results = {}

try:
    response = requests.post(API_URL, json=test_data)
    response.raise_for_status()
    result = response.json()["result"]
    assert "Predicted result for" in result
    test_results["status"] = "success"
    test_results["details"] = result
except Exception as e:
    test_results["status"] = "failed"
    test_results["details"] = str(e)

# 테스트 결과 저장
with open("test_results.json", "w") as f:
    json.dump(test_results, f, indent=4)
