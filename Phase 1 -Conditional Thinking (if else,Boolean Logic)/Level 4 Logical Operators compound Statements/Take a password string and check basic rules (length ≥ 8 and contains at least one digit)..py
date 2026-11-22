password = input("Enter a password: ")

has_digit = False

for chac in password:
    if chac.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit:
    print("Valid password")
else:
    print("Invalid password")