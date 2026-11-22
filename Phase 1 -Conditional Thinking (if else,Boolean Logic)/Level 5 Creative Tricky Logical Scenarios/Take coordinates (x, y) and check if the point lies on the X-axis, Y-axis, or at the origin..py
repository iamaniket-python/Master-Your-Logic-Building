x=int(input("Enter a First Number= "))
y=int(input("Enter a second Number= "))

if x == 0 and y == 0:
    print("origin ")
elif x != 0 and y == 0:
    print("x-axis")
elif x == 0 and y !=0:
    print("y-axis")
else:
    print("Point lies on neither axis")