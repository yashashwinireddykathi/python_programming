def palen(n):
    s=0
    t=n
    while(t>0):
        r=t%10
        s=s*10+r
        t//=10
    if(s==n):
        print("palen")
    else:
        print("not palen")
palen(121)
