n = int(input("Enter a number = "))
original = n

count = 0
temp = n

while temp > 0:
    count += 1
    temp = temp // 10


total = 0
temp = n

while temp > 0:
    digit = temp % 10
    total += digit ** count
    temp = temp // 10


if total == original:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
