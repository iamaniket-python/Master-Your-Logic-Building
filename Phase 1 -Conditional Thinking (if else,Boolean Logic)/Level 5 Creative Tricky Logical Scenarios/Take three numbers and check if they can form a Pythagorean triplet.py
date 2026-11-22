x=int(input("Enter a First Number= "))
y=int(input("Enter a Second Number= "))
z=int(input("Enter a Third Number= "))

largest =max(x,y,z)

if largest == x:
    if y**2 + z **2 == x**2:
        print("Pythagorean Triplet")
    else:
        print("Not a Pythagorean Triplet")

elif largest == y:
    if x**2 + z**2 == y**2:
        print("Pythagorean Triplet")
    else:
        print("Not a Pythagorean Triplet")

else:
    if x**2 + y**2 == z**2:
        print("Pythagorean Triplet")
    else:
        print("Not a Pythagorean Triplet")

