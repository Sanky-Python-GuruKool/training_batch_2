# import time
# import math
# start = time.time()
# print(math.sqrt(144))
# print(math.factorial(50))

# from colorama import Fore, Back, Style

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# import random 
# # print("*"*100)
# # print()
# # print(random.randint(1,1000))

# names = ["Sanket", "Akshay", "Priya", "Pooja"]

# print(Fore.RED + random.choice(names))
# print(Style.RESET_ALL)


# import secrets

# otp = secrets.randbelow(10000) + 10000

# print(Fore.RED + str(otp))
# print(Style.RESET_ALL)


# import getpass
# pwd  = getpass.getpass("Enter password ")

# print(pwd)


# import time

# print("Loading...")
# time.sleep(5)  # Pauses the script for 2.5 seconds
# print("Done!")

# stop = time.time()


# print(start, stop)

# print(stop - start)


# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%d-%m-%Y"))
# print(now.strftime("%H:%M:%S"))


import calendar

# Print a specific month's calendar
print(calendar.month(2026, 10))
