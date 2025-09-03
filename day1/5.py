p=int(input("enter principal amount\n"))
t=int(input("enter the time in months\n"))
r=int(input("enter the rate of interest\n"))
si=(p*t*r)/100
a=p+si
print("the simple interest:\n",si)
print("the amount in hands:\n",a)