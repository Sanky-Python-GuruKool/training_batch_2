import random
from colorama import Fore, Style

print("*" * 100)
print()
print(random.randint(1, 1000))

names = ["Sanket", "Akshay", "Priya", "Pooja"]

print(Fore.RED + random.choice(names))
print(Style.RESET_ALL)
