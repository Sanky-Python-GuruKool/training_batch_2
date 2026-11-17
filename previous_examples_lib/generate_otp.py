import secrets
from colorama import Fore, Style

otp = secrets.randbelow(10000) + 10000

print(Fore.RED + str(otp))
print(Style.RESET_ALL)
