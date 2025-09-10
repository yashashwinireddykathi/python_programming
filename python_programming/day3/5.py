def deletion():
    list=[1,2,3,4,5]
    a=int(input("enter position"))
    if a <=len(list)+1:
        list.pop(a)
    else:
        print("can't remove")
    print(list)
deletion()