#greatest of 3 nos
def greater(a,b,c):
    if(a>b):
        if(a>c):
            print(a," is greater")
        else:
            print(c ," is greater")
    elif(b>c):
        print(b," is greater")
    else:
        print(c," is greater")
greater(5,12,6)
greater(10,2,3)
greater(3,4,10)
greater(-1,-2,-3)