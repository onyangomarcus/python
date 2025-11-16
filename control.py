# age = int(input("Enter your age: ")) 

"""
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
"""
# status = "Adult" if age >= 18 else "Minor"

# print(status)
"""
x = int(input("Enter x: "))
if x > 5 and x < 15:
    print("x is between 5 and 15")
else:
    print("X is off the range")
"""

word = input("Enter a word: ")
char = 'e'

if char in word:
    print(f"{char} was found in {word}")
else:
    print(f"{char} was not found in {word}")