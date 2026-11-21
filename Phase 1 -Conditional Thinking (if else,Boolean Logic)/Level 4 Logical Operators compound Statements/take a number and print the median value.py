x=int(input("Enter a first Number= "))
y=int(input("Enter a Second Number= "))
z=int(input("Enter a Third Number= "))

if x <= y <= z or z <= y <= x:
    print("Median is", y)
elif y <= x <= z or z <= x <= y:
    print("Median is", x)
else:
    print("Median is", z)