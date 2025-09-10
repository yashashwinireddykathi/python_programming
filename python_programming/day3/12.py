def s():
    a=input("enter the string")
    l=0
    d=0
    s=0
    for i in a:
        if(i.isalpha()):
            l+=1
        elif(i.isdigit()):
            d+=1
        else:
            s+=1
    print("Number of letters:", l)
    print("Number of digits:", d)
    print("Number of special characters:", s)
s()
        

