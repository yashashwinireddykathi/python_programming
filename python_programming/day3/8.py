#count total no of duplicete elemnets in the list
def dup(lst):
    l={''}
    for i in range(len(lst)):
        c=0
        for j in range(len(lst)):
            if lst[i]==lst[j]:
                c=c+1
        if c>1:
            l.add(lst[i])  
    print("Total duplicates:",len(l))
dup([1,1,2,3,2,3])