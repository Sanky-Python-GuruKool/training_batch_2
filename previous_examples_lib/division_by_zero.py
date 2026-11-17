try:
    number1 = int(input("Enter Number 1 : "))
    number2 = int(input("Enter Number 2 : "))
    result = number1 / number2
    print(f"Result is {result}")
except Exception:
    print("You can't divide by zero")
