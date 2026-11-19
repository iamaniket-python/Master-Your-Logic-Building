x = int(input("Enter a first number="))
y = int(input("Enter a second number="))

x_even = x % 2 == 0
y_even = y % 2 == 0

if x_even and y_even:
    print("both are even")
elif not x_even and not y_even:
    print("both are odd")
else:
    print(f"x is {'even' if x_even else 'odd'}, y is {'even' if y_even else 'odd'}")



