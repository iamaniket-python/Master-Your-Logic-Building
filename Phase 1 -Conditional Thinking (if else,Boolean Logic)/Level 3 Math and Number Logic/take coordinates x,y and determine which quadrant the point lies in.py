x=int(input("Enter a First Number="))
y=int(input("Enter a Second Number="))

if x > 0 and y > 0:
    print("1st quadrant")
elif x < 0 and y > 0:
    print("2nd quadrant")
elif x < 0 and y < 0:
    print("3rd quadrant")
elif x > 0 and y < 0:
    print("4th quadrant")
else:
    print("Point is on an axis or at the origin")