import requests


def test_conversion():
    url = "http://localhost:8000/convert"
    payload = {
        "amount": 300,
        "currency": "USD",
        "target_currency": "JPY"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Converted Amount: {response.json()['amount']}")
    else:
        print(f"Error: {response.json()}")


if __name__ == "__main__":
    test_conversion()
