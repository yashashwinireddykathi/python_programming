#count no of digits
def sum(n):
    s=0
    while n>0:
        r=n%10
        s+=1
        n=n//10
    print(s)
sum(123)