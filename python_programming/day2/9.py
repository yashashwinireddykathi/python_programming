#prime or not
def prime(n):
    if(n==0 or n==1):
        print(n,"is not prime")
    else:
        i=2
        b=True
        while i<n:
            if(n%i)==0:
                b=False
                break
            i=i+1
        if b:
            print(n,"is prime")
        else:
            print(n,"is not prime")
prime(6)
prime(3)
prime(1)
prime(0)