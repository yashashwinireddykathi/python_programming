s=input("enter the string")
l=[]
c=input("enter the char to find the occurrences")
for i in range(len(s)):
    if s[i]==c:
        l.append(i)
print(l)