a=int(input("Enter a first trangle="))
b=int(input("Enter a second trangle="))
c=int(input("Enter a third trangle="))


if a > 0 and b > 0 and c > 0 and (a + b > c) and (b + c > a) and (a + c > b):
    print("it is valid")

else:
    print("not valid")