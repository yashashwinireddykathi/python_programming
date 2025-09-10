#count vowels and consonents
def s(a):
    c=0
    b=0
    if a.isalpha():
        for i in a:
            if(i=='a'or i=='e' or i=='i'or i=='o' or i=='e'or i=='u'):
                c+=1
            else:
                b+=1
    print("no of vowels",c)
    print("no of consonents",b)
s(input("enter a string"))