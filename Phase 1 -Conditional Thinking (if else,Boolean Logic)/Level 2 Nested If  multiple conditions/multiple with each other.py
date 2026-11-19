num1=int(input("Enter a first Number="))
num2=int(input("Enter a second Number="))

if (num2 != 0 and num1 % num2 == 0) or (num1 != 0 and num2 % num1 == 0):
    print("yes both are multiply")
else:
    print("no both cant multiply")
