#simple if
a=30
b=20
if a>b :
    print("a is big")
print("tq")

#if else
if a>b:
    print('a is big')
else:
    print('b is big')
    
#1)even or odd
def even(x):
    if(x%2==0):
        print(x," is even")
    else:
        print(x," is odd")
even(1)

#2)neg or pos no
def neg(x):
    if(x>0):
        print(x," is positive")
    elif(x<0):
        print(x," is negative")
    else:
        print("zero")
neg(10)

#3)div by 5 and 11
def div(x):
    if(x%5==0 and x%11==0):
        print(x," is divibile by both 5 and 11")
    else:
        print(x," is not divisible by 5 and 11")
div(55)