x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if y > z and y > x:
    print(y,"yes it is largest")

elif y < x and y < z:
    print(y,'is smallest')

else:
    print(y, "is neither largest nor smallest")