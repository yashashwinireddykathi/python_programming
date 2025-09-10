list=[1,2,3,4]
m=list[0]
s=list[0]
for i in list:
    if(i>m):
        s=m
        m=i
    elif(i>m and i!=m):
        s=i
print(s)