x=int(input("Enter a Number="))

if x % 5 == 0 and x % 3 ==0:
    print("FizzBuzz")
elif x % 5 == 0:
    print("Buzz")
elif x % 3 ==0:
    print("fizz")