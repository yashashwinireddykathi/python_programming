def notes(amount):
    denominations = [2000, 500, 50, 10, 5, 2, 1]
    count = 0
    for note in denominations:
        if amount >= note:
            note_count = amount // note
            count += note_count
            amount = amount % note
    
    return count
x = int(input("Enter amount: "))
print("Total number of notes/coins:", notes(x))
