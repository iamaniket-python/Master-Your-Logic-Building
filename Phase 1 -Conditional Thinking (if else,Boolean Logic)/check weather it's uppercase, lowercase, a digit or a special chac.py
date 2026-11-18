char = input("Enter a character = ")


if len(char) == 1:
    if char.isupper():
        print("It is uppercase")
    elif char.islower():
        print("It is lowercase")
    elif char.isdigit():
        print("It is a number/digit")
    else:
        print("It is a special symbol")
else:
    print("Please enter only a single character.")

