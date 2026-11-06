# # # from faker import Faker
# # # names = []
# # # fake = Faker()

# # # for i in range(100):
# # #     names.append(fake.name())



# # # count = 1
# # # for i in names:
# # #     if count  == 5:
# # #         print("Found", i)
# # #         break
# # #     print(count)
# # #     count = count + 1


# # roll_numbers = [101, 102, 103, 104, 105]

# # for roll in roll_numbers:
# #     print("Checking:", roll)
# #     break
# # print("Search completed")





# # def find_product(products, target):
# #     for product in products:
# #         if product == target:
# #             print(target, "is available")
# #             break
# #     print("Product check finished")

# # find_product(["Pen", "Book", "Pencil"], "Book")



# attempt = 1

# while attempt <= 5:
#     print("Trying to connect... Attempt", attempt)

#     if attempt == 3:
#         print("Connected!")
#         break

#     attempt += 1



# marks = [75, -1, 2, 3,45, 68]

# for i in marks:
#     if i < 0 :
#         continue
    
#     if i > 70:
#         print("distinction")
#     elif i > 40 and i < 70:
#         print("Pass")
#     elif i > 0 and i < 20:
#         print("Please work hard it's your Future !!")
#     else:
#         print("Fail")


# age = 17

# if age < 18:
#     pass  # Under-18 users ke liye logic baad mein likhenge
# else:
#     print("Adult user")

# print("Age checked")

# if 10 > 2:
#     num = 5

# def show_student():
    
#     num = num +  10
#     print(f"Inside Func {num}")

# show_student()
# print("Outside", num)


# total_visit = 0

# def museum_vist():
#     global total_visit
#     total_visit = total_visit + 1
#     print(total_visit)


# museum_vist()
# museum_vist()
# museum_vist()
# museum_vist()





# def student_count():
#     students = ["Aarya", "Rohan", "Neha"]
#     print("Total students:", len(students))

# student_count()


def classroom():
    teacher = "Sanket Sir"
    def introduce():
        nonlocal teacher
        teacher = teacher + " Python "
        print("Teacher:", teacher)
        

    introduce()
    print("Teacher:", teacher)

classroom()


