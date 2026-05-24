import requests
import time

URL = "http://localhost:4499"

def check_app():
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            print(f"✅ APP UP | Status Code: {response.status_code}")
        else:
            print(f"⚠ APP ISSUE | Status Code: {response.status_code}")

    except requests.exceptions.RequestException:
        print("❌ APP DOWN | No Response")

if __name__ == "__main__":
    while True:
        check_app()
        time.sleep(5)