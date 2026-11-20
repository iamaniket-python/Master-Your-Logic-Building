x = int(input("Enter  number: "))

if x < 9:
    print("it has single digit")
elif x < 99:
    print("it has double digit")
elif x > 100:
    print("it has triple digit")
else:
    print("please enter 1 to 999")

