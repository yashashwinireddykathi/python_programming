#sum of natural nos
def sum(n):
    s=0
    i=0
    while i<=n:
        s=s+i
        i=i+1
    return s
print(sum(5))