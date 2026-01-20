import requests
import sys

API_URL = "https://reqres.in/api/users/2" #Dummy url
TIMEOUT = 5

def validate_api_health():
    try:
        response = requests.get(API_URL, timeout=TIMEOUT)

        if response.status_code != 200:
            print(f"API returned unexpected status code: {response.status_code}")
            sys.exit(1)

        data = response.json()

        if "data" not in data:
            print("API response structure is invalid")
            sys.exit(1)

        print("API status check passed.")

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_api_health()
