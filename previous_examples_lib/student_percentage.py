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
