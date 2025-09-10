list=[1,2,3,-4,-5]
c1=0
c2=0
for i in list:
    if i%2==0:
        c1+=1
    else:
        c2+=1
print("even nos:",c1)
print("odd nos:",c2)