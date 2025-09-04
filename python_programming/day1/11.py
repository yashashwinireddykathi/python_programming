#fun with args and no return
def add(a,b):
    print(a+b)
add(10,20)      # or x=10,y=20 then add(x,y)
#--------------------
def dis(a):
    print(a*0.62)
dis(1000)
#--------------------
def days(a):
    print("years:",round(a/365,2))
    print("months:",round(a/30,2))
days(int(input("enter no")))
days(45)
    