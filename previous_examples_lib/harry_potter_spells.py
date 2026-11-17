import requests


def get_spell():
    response = requests.delete('https://potterapi-fedeperin.vercel.app/en/spells', "ksjdhcv")
    spells = response.json()
    return spells


spells = get_spell()
print("Welcome to teh Harry Potter World ")
spell = input("Enter a Spell name ")

print("This spell does the following work ........")

for i in spells:
    if i["spell"] == spell:
        print(i["use"])
