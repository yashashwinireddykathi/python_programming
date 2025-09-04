#student pass or fail based on average marks
sn=int(input("enter the student no"))
sname=input("enter the name of the student")
math=int(input("enter math marks"))
phy=int(input("enter phy marks"))
chem=int(input("enter chem marks"))
t=math+phy+chem
avg=t/3.0
print("student no:",sn)
print("student name:",sname)
print("math marks:",math)
print("physics marks:",phy)
print("chem marks:",chem)
print("total marks:",t)
#print(f"average marks:{avg:.2f}")
x=(round(avg,2))
print(x)
if(x<40 or  x>100):
    print("fail")
else:
    print("Pass")
    if(x>=40 and x<=50):
        print("Grade c")
    elif(x>50 and x<=70):
        print("Grade B")
    elif(x>70 and x<=80):
        print("Grade A")
    elif(x>80):
        print("Distension")