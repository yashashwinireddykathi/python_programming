#all prime factors of no
def prime(n):
    if(n==1):
        return False
    f=True
    for j in range(2,n):
        if n%j==0:
            f=False
            break
    return f
def primefact(n):
    for j in range(1,n+1):
        if(n%j==0 and prime(j)):
             print(j)
primefact(10)