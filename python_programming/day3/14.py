def cw():
    s=input("enter the string")
    c=1
    for i in s:
        if i=="," or i==" " or i=="\n":
            c+=1
    print("no of words:",c)
cw()