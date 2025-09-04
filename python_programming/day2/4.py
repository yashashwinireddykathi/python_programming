name = input("Enter name: ")
pmr = int(input("Enter present month reading: "))
lmr = int(input("Enter last month reading: "))
t = abs(pmr - lmr)
if 0 <= t <= 50:
    bill = t * 3.80
elif 51 <= t <= 100:
    bill = (50 * 3.80) + (t - 50) * 4.20
elif 101 <= t <= 200:
    bill = (50 * 3.80) + (50 * 4.20) + (t - 100) * 5.10
elif 201 <= t <= 300:
    bill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + (t - 200) * 6.30
else:
    bill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + (100 * 6.30) + (t - 300) * 7.50
print(f"Name: {name}")
print("Total Units Consumed:", t)
print("Bill Amount: ₹", round(bill, 2))
