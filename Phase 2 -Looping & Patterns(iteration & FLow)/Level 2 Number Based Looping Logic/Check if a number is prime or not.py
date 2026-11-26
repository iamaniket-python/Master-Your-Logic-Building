n=int(input("Enter a Number= "))

is_prime= True

if n <=1:
    is_prime=False

else:
    for i in range(1, n):
        if n % i ==0:
            is_prime=False
            break

if is_prime:
    print("prime number")
else:
    print("not Prime")