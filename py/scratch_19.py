"""
Professional check up software
Author: Leonardo Miguel
Description:
    This app validates a person and his age
of a professional in workplace market.
Tools: Pycharm & w3Schools
"""

# Declarations

# Just a Hello for user
greetings = "Hello, how are you?"

# Here the user will type his name
person_name = input("Please, type your name: ")

# Here the user will type his age
pro_area = int(input("Type your age, please: "))

print(greetings)

# Conditionals

# This line do a verification if the user has 0 to 12 years old.

if pro_area <= 12:
    print(f"Hey, {person_name} your professional age area is: {pro_area} - Child")
    input("Press Enter to shutdown...")

# This line do a verification if the user has 13 to 18 years old.

elif pro_area <= 17:
    print(f"Hey, {person_name} your professional age area is: {pro_area} - Teen")
    input("Press Enter to shutdown...")

# This line do a verification if the user has 18 to 24 years old.

elif pro_area <= 24:
    print(f"Hey, {person_name} your professional age area is: {pro_area} - Teen II")
    input("Press Enter to shutdown...")

# This line do a verification if the user has 24 to 30 years old.

elif pro_area <= 30:
    print(f"Hey, {person_name} your professional age area is: {pro_area} - Professional")
    input("Press Enter to shutdown...")

# This line do a verification if the user type 0 (Oh)

elif pro_area <= 0:
    print("Are you a baby?")
    input("Press Enter to shutdown...")

# This line do a verification if the user has 34 or more years old.

else:
    print(f"Hey, {person_name} your professional age area is: {pro_area} - Senior")
    input("Press Enter to shutdown...")

# end
