#lowest frequency
s = input("Enter the string: ")
l = ''
m=len(s)+1
for ch in s:
        count = 0
        for c in s:
            if ch == c:
                count += 1
        if count<m:
             m=count
             l=ch
print(l)          