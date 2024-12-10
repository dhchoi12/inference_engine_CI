import requests
import argparse

def run_test(url):
    test_data = {
        "text": "Test from Blob Test Tool"
    }

    try:
        response = requests.post(f"{url}/inference", json=test_data)
        response.raise_for_status()
        print("Test Passed:", response.json()["result"])
    except Exception as e:
        print("Test Failed:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Inference Engine URL")
    args = parser.parse_args()
    run_test(args.url)
