def find_product(products, target):
    for product in products:
        if product == target:
            print(target, "is available")
            break
    print("Product check finished")


find_product(["Pen", "Book", "Pencil"], "Book")
