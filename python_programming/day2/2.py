#program to check whether it is alphabet or digit or special charecter
def charac(ch):
    if ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
        print("alphabet")
    elif('0'<=ch<='9'):
        print("digit")
    else:
        print("special character")
charac(input("enter\n"))