#strong no
def strong(n):
    for i in range(1,n+1):
        t=i
        while(t>0):
            a=1
            r=t%10
            for j in range(1,r+1):
                a=a*j
            s=s+a
            t//=10
        if(s==i):
            print(i)
strong(100)