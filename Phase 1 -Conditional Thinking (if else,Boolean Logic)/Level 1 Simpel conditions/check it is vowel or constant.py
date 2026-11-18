name = input("Enter a Name = ")
name = name.lower()

vowel_found = False

for digit in name:
    if digit in "aeiou":
        vowel_found = True
        break

if vowel_found:
    print("it has vowels")
else:
    print("it has no vowels")