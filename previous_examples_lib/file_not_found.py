try:
    for i in range(1, 201):
        f = open("abc.txt")
        print(f.read())
        print(10 / 0)
except FileNotFoundError:
    print("Oops Sopmething wrong file not found")
finally:
    f.close()
