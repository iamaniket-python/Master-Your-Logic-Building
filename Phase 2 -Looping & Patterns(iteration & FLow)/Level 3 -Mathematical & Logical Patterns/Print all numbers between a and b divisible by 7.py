a=int(input("Enter a first Number= "))
b=int(input("Enter a Second Number= "))

for i in range(a , b+1):
    if i % 7 == 0:
        print(i,end=" ")
