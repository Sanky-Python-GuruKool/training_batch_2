from colorama import Fore, Back, Style

students = ["Neha", "Diya", "Jay", "Rahul"]
try:
    user = int(input("Enter index number for person whose result you wana see (0-3)"))
    print(f"Result of {students[user]}")
except Exception:
    print(Fore.RED + "Only Allowed values are 0 - 3")
    print(Style.RESET_ALL)

print("Thank You for Using our Servioce")
