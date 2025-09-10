#library management system
def dict():
    d={}
    while True:
        print("library management system")
        print("1.add a book")
        print("2.remove a book")
        print("3.search a book")
        print("4.update the title")
        print("5.display all books")
        print("6.count the total no of books")
        print("7.chech if a book title exists")
        a=int(input("enter the choice (1-7)"))
        if(a==1):
            k=input("enter the key ")
            v=input("enter the value")
            if k in d:
                print(k,"already exists")
            else:
                d[k]=v
        elif(a==2):
            k=input("enter the key ")
            if k in d:
                d.pop(k)
            else:
                print(k,"doesn't exist")
        elif a==3:
            k=input("enter the key ")
            if k in d:
                print("book is found",d[k])
            else:
                print("book not found")
        elif a==4:
            k=input("enter the key ")
            if k in d:
                d[k]=input("enter new title")
            else:
                print("book not found")
        elif a==5:
            print(d)
        elif a==6:
            print("total no of books:",len(d))
        elif (a==7):
            v=input("enter the book title")
            if v in d.values():
                print("book exists")
            else:
                print("book doesn't exist")
        else:
            exit()
dict()

