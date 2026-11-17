import requests

url = "https://dog.ceo/api/breeds/image/rando"

response = requests.get(url)

if response.status_code == 200:
    resp = response.json()
    print(resp)
else:
    print(f"We got an error {response.status_code}")
