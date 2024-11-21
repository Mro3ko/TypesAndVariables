first = input("Enter first letter: ")
last = input("Enter last letter: ")
first=first.upper()
last=last.upper()
first_letter_code=ord(first)
last_letter_code=ord(last)
number_of_letters=last_letter_code-first_letter_code-1
if first==last:
    print(0)
else:
    print(number_of_letters)