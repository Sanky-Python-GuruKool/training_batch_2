def classroom():
    teacher = "Sanket Sir"

    def introduce():
        nonlocal teacher
        teacher = teacher + " Python "
        print("Teacher:", teacher)

    introduce()
    print("Teacher:", teacher)


classroom()
