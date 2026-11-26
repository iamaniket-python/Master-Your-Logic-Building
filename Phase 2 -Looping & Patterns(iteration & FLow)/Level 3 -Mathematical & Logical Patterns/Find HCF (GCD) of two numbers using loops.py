a=int(input("Enter a first Number= "))
b=int(input("Enter a Second Number= "))

hcf= 1

for i in range(1, min(a ,b)+1):
    if a % i == 0 and b % i == 0:
        hcf =1

print("HCF =",hcf)