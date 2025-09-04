#multiplication table
def mul(n):
    for i in range(1,10+1):
        print(n,"X",i,"=",n*i)
mul(int(input()))