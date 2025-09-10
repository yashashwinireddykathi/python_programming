#s=set()
#for i in range(2):
    #s.add(input("enter set elements"))
#print(s)

day1 = ["jagu@example.com", "laha@example.com", "Mama@example.com", "Jagu@example.com"]
day2 = ["LAHA@example.com", "shyam@example.com", "sai@example.com"]
day3 = ["jagu@example.com", "bhag@example.com", "Rushi@example.com", "Laha@example.com"]

def clist(lst):
    return set(email.lower() for email in lst)
d1 = clist(day1)
d2 = clist(day2)
d3 = clist(day3)
unique = d1 | d2 | d3
three = d1 & d2 & d3
exactly_one = (d1- d2- d3) | (d2 - d1 - d3) | (d3 - d1 - d2)
d1_d2 = d1 & d2
d2_d3 = d2 & d3
d1_d3 = d1 & d3
print("Final")
print(f"Total unique attendees: {len(unique)}")
print("List:", sorted(unique))
print()
print(f"Attendees who attended all three days: {len(three)}")
print("List:", sorted(three))
print()
print(f"Attendees who attended exactly one day: {len(exactly_one)}")
print("List:", sorted(exactly_one))
print()
print(f"Pairwise overlaps:")
print(f"Day1 & Day2: {len(d1_d2)} -> {sorted(d1_d2)}")
print(f"Day2 & Day3: {len(d2_d3)} -> {sorted(d2_d3)}")
print(f"Day1 & Day3: {len(d1_d3)} -> {sorted(d1_d3)}")