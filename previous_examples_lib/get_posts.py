import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, timeout=10)

print(response.status_code)
if response.status_code == 200:
    var = response.json()
    print(type(var))
    print(var)
for i in var:
    print(i["userId"])
