import requests
import json

# 테스트 결과 저장
test_results = {}

# 테스트 데이터
test_data = {
    "text": "Hello from GitHub Actions"
}

# 테스트 실행
try:
    response = requests.post("http://localhost:5000/inference", json=test_data)
    assert response.status_code == 200
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
