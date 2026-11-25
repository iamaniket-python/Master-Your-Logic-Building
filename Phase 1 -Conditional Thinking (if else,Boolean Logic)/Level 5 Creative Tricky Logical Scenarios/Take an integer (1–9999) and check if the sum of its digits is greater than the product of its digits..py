n=int(input("Enter a Number= "))

total =0
prod=1

while n > 0:
    digit = n % 10

    total = total + digit
    prod = prod * digit

    n = n //10

if total > prod:
    print("sum is greater than product")
else:
    print("sum is not greater than product")