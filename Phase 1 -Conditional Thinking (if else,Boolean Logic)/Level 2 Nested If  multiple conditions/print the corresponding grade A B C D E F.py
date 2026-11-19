marks=int(input("Enter a Marks of a student="))

if marks < 30:
    print("Grade F")
elif marks <= 40:
    print("grade E")
elif marks <= 55:
    print("grade D")
elif marks <= 70:
    print("grade C")
elif marks <= 80:
    print("grade B")
elif marks > 80:
    print("grade A")
else:
    print("Please enter some marks")

