year=int(input("Enter a Year="))


if year in { 1, 3 , 5, 6, 8 ,10 ,12}:
    print(year,"it has 31 days")

elif year in { 4, 6 , 9 ,30}:
    print(year,"it has 30 days")

else:
    print("please enter right Year")