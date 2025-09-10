def students():
    t=[(563,"yash",80),(516,"jag",20),(502,"akh",70),(510,"deek",85)]
    highest = t[0]
    for i in range (len(t)):
        if t[i][2] > highest[2]:
            highest = t[i]
    print("Highest marks student:", highest[1], highest[2])
    print("Students with marks > 75:")
    for s in t:
        if s[2] > 70:
            print(s[0],s[1], s[2])
students()
