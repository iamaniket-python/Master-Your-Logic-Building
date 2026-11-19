hrs = int(input("Enter a Hrs="))

if hrs < 0 or hrs > 23:
    print("Invalid hour! Enter between 0 and 23.")
elif hrs < 12:
    print("Good Morning")
elif hrs < 17:
    print("Good Afternoon")
elif hrs < 21:
    print("Good Evening")
else:
    print("Good Night")
