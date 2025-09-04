def palen(n):
    for i in range(1,n+1):
        s=0
        t=i
        while(t>0):
            r=t%10
            s=s*10+r
            t//=10
        if(s==i):
            print(i)
palen(150)
