def string():
    str=input("enter the string")
    c=0
    for i in str:
        c+=1
    print("length of string:",c)
    str1=input("enter the string")
    if(str==str1):
        print("equal")
    else:
        print("Unequal")
    print(str+str1)
string()