attempt = 1

while attempt <= 5:
    print("Trying to connect... Attempt", attempt)

    if attempt == 3:
        print("Connected!")
        break

    attempt += 1
