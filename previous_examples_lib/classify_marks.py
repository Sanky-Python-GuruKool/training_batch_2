marks = [75, -1, 2, 3, 45, 68]

for i in marks:
    if i < 0:
        continue

    if i > 70:
        print("distinction")
    elif i > 40 and i < 70:
        print("Pass")
    elif i > 0 and i < 20:
        print("Please work hard it's your Future !!")
    else:
        print("Fail")
