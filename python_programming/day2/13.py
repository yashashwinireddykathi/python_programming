#first and last digit of no
def fandn(x):
    n=x
    while x!=0:
        r=x%10
        x=x//10
    a=n%10
    print("first no:",r)
    print("last no:",a)
    print("sum:",a+r)
fandn(134)