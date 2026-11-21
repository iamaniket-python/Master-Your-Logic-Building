num= int(input("Enter a number="))

if num in {1 ,2, 3, 4, 5}:
    print("it is a weekday")
elif num in {6 ,7}:
    print("it's a weekend")
else:
    print("please enter number between 1 to 7")