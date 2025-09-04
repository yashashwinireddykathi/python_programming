#factorial of a given no
def fact(n):
    f=1
    for i in range(1,n+1):
            f=f*i
            i=i-1
    return f 
print(fact(5))
#using while loop
def f(n):
    fa=1
    while n>1:
        fa=fa*n
        n=n-1
    return fa
print(f(5))