# try:
#     number1 = int(input("Enter Number 1 : "))
#     number2 = int(input("Enter Number 2 : "))
#     result = number1/number2
#     print(f"Result is {result}")
# except Exception:
#     print("You can't divide by zero")



# from colorama import Fore, Back, Style



# students = ["Neha", "Diya", "Jay", "Rahul"]
# try:
#     user = int(input("Enter index number for person whose result you wana see (0-3)"))
#     print(f"Result of {students[user]}")
# except Exception:
#     print(Fore.RED + "Only Allowed values are 0 - 3")
#     print(Style.RESET_ALL)

# print("Thank You for Using our Servioce")




# try:
#     for i in range(1,201):
#         f = open("abc.txt")
#         print(f.read())
#         print(10/0)
# except FileNotFoundError:
#     print("Oops Sopmething wrong file not found")
# finally:
#     f.close()


try:
    print(10/0)
    print("I am in try")
    
except Exception as e:
    print("I am in Except", e)
finally:
    print("Thank You for Using our Service")







try:
    name = input("Student name: ")
    marks = int(input("Marks: "))

    try:
        total = int(input("Total marks: "))
        print("Percentage:", marks / total * 100)

    except ZeroDivisionError:
        print("Total marks zero nahi ho sakte.")

except ValueError:
    print("Marks aur total marks numbers hone chahiye.")