def f(x):
    for i in range(x,0,-1):
        if x%i==0:
            return i
    return 1
print(f(7)+f(9))