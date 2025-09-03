#leap year or not
def leap(x):
    if((x%4==0 and x%100!=0) or x%400==0):
        print(x," is leap year")
    else:
        print(x,"is not leap year")
leap(2000)
leap(2024)
#alphabet or not
def alpha(ch):
    if ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
        print("alphabet")
    else:
        print("not")
alpha('d')
#consonent 
def alpha(st):
    if(st=='a'or st=='e' or st=='i' or st=='o' or st=='u'):
        print( "vowel")
    else:
        print("consonent")
alpha('a')