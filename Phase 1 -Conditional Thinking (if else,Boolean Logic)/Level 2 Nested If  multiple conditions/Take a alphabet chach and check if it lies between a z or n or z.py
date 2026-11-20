char=input("Enter a name=").lower()

for digit in char:
    if digit  in  {'a', 'm', 'n', 'z'}:
        print("yes it has")
        break
else:
    print("not it does not have")