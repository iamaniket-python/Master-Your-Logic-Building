day = int(input("Enter day: "))
month = int(input("Enter month: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >= 1 and day <= 31:
        print("Valid date")
    else:
        print("Invalid date")

elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        print("Valid date")
    else:
        print("Invalid date")

elif month == 2:
    if day >= 1 and day <= 28:
        print("Valid date")
    else:
        print("Invalid date")

else:
    print("Invalid month")