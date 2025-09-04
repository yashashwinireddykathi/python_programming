def arm(n):
    for i in range(1,n+1):
        s=0
        t=i
        #b=len(str(i))
        while(t>0):
            r=t%10
            s=s+r**3
            t//=10
        if(s==i):
            print(i)
arm(1000)
