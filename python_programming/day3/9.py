#You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
#1.Add a product to the cart.
#2.Remove a product from the cart 
#3.Search for a product in the cart 
#4.Display all products in the cart
#5.Show the total number of products in the cart
#Cart Operations:
#1. Add Product
#2. Remove Product
#3. Search Product
#4. Display Cart
#5. Count Products
#6. Exit
#Enter choice: 1
#Enter product to add: Laptop
#Product 'Laptop' added to cart.
#Enter choice: 1
#Enter product to add: Phone
#Product 'Phone' added to cart.
#Enter choice: 4
#Cart: ['Laptop', 'Phone'] 
#Enter choice: 3
#Enter product to search: Phone
#Yes, 'Phone' is in the cart.
#Enter choice: 5
#Total products in cart: 2
def e_commerce():
    l=[]
    while True:
        print("\n Cart Operations")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Search product in cart")
        print("4. Display cart")
        print("5. Count total products in cart")
        print("6.Sort the casrt items")
        print("7.clear the cart")
        print("8. Exit")
        a=int(input("enter the choice between 1-8\n"))
        if(a==1):
            ele=input("enter the product to add")
            l.append(ele)
            print("product",ele," is added to cart")
        elif a==2:
            ele=input("enter the element to remove")
            if ele in l:
                l.remove(ele)
                print(ele," is removed from the cart")
            else:
                print(ele," is not present in the list")
        elif a==3:
            ele=input("enter the product to search")
            if ele in l:
                print("Yes",ele," is in the cart")
            else:
                print("NO",ele,"is not present in cart")
        elif a==4:
            print("cart:",l)
        elif a==5:
            print("Total products in cart:",len(l))
        elif a==6:
            print("Cart is sorted",l.sort())
        elif a==7:
            print("cart is cleared",l.clear())
        elif a==8:
            exit()
e_commerce()  