#prime no from 1 to n
def prime(n):
    c=0
    for i in range(2,n):
        b=True
        for j in range(2,i):
            if(i%j==0):
                b=False
                break
        if(b):
            print(i,end=" ")
            c+=1
    print("\ncount of primes:",c)
prime(7)
