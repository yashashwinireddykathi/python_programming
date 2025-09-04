name=input("enter name")
pmr=int(input("enter present month reading"))
lmr=int(input("enter last month reading"))
t=abs(pmr-lmr)
c=t*3.80
print("name:",name,"\n","pmr:",pmr,"\n","lmr:",lmr,"\n","total units:",t,"\n","current bill:",round(c,2))