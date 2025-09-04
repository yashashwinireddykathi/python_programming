#display n natural nos using while loop
def natural(n):
    i=1
    while i<=n:
        print(i)
        i=i+1
natural(10)

#print all alphabtes from a to z
def alphabets():
    letters = "abcdefghijklmnopqrstuvwxyz"  
    i = 0
    while i < len(letters):
        print(letters[i], end=" ")
        i += 1
alphabets()