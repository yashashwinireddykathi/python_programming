#strong no
def strong(n):
    s=0
    t=n
    while t>0:
        a=1
        r=t%10
        for i in range(1,r+1):
            a=a*i
        s=s+a
        t//=10
    if(s==n):
        print("Strong")
    else:
        print("not strong")
strong(145)