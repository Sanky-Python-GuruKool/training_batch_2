# # import requests

# # url = "https://jsonplaceholder.typicode.com/posts"

# # response = requests.get(url, timeout=10)

# # print(response.status_code)
# # if response.status_code == 200 :
# #     var = response.json()
# #     print(type(var))
# #     print(var)
# # for i in var:
# #     print(i["userId"])



# import requests

# def get_spell():
#     response = requests.delete('https://potterapi-fedeperin.vercel.app/en/spells', "ksjdhcv")
#     spells = response.json()
#     return spells
# spells = get_spell()
# print("Welcome to teh Harry Potter World ")
# spell = input("Enter a Spell name ")

# print("This spell does the following work ........")

# for i in spells:
#     if i["spell"] == spell:
#         print(i["use"])



import requests

url = "https://dog.ceo/api/breeds/image/rando"

response = requests.get(url)

if response.status_code == 200:
    resp = response.json()
    print(resp)
else:
    print(f"We got an error {response.status_code}")