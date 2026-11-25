n=int(input("Enter a Number= "))
original =n
palidrome=0

while n > 0:
    digit = n % 10
    palidrome = palidrome * 10 + digit
    n = n // 10

if palidrome == original:
    print("it a palidrome")
else:
    print("not palidrome")


