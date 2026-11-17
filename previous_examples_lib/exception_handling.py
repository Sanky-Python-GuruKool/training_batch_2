try:
    print(10 / 0)
    print("I am in try")

except Exception as e:
    print("I am in Except", e)
finally:
    print("Thank You for Using our Service")
