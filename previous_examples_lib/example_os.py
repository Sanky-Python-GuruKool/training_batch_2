import os

print(os.getcwd())

os.makedirs("New_Directory", exist_ok = True)

for i in os.listdir("."):
    print(i)
    print(os.path.getsize(i))




