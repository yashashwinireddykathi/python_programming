
s = input("Enter the string: ")
l = []
for ch in s:
    if ch not in l:  
        count = 0
        for c in s:
            if ch == c:
                count += 1
        print(f"{ch}{count}", end="")
        l.append(ch)
