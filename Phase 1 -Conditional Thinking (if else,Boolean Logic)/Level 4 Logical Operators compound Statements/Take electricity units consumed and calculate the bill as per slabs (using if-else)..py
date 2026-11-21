units = int(input("Enter electricity units consumed = "))

if units >= 0 and units <= 100:
    bill = units * 5
elif units > 100 and units <= 200:
    bill = units * 7
elif units > 200:
    bill = units * 10
else:
    bill = 0
    print("Invalid units")

if units >= 0:
    print("Total electricity bill =", bill)