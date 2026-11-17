from faker import Faker

names = []
fake = Faker()

for i in range(100):
    names.append(fake.name())

count = 1
for i in names:
    if count == 5:
        print("Found", i)
        break
    print(count)
    count = count + 1
