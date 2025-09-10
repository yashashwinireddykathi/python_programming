# unique elments
def freq(lst):
    l = []
    for i in range(len(lst)):
        c = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                c += 1
        if c==1:
            l.append(lst[i])
    print(l)
freq([1, 1, 2, 3, 4])
