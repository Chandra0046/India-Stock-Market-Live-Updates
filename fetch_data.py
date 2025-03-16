import requests

API_KEY = "0afce234-885a-425c-bf15-12cd928aea13"
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIyMDMzODUiLCJqdGkiOiI2N2Q2NmQ2OWQwNGViMzEwMWI3NTc2ZWEiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzQyMTA1OTYxLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDIxNjI0MDB9.Z1PI8TFn55YkAUnEjjd78rOH936VctB55HxnkkuZFVM"

def fetch_indices():
    url = "https://api.upstox.com/market_data"  # Replace with the correct Upstox endpoint
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return {}

data = fetch_indices()
print(data)  # You can view the data structure
