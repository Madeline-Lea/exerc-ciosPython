"""
Validation Program
Author - Leonard Miguel
Date - 04/02/2022
Description - This program has the solution
to validate an age by buying a ticket.
"""
# declaration

age = input("What's your age, type please: ")  # initial phase of program that do the magic.

ageInt = int(age)  # this cast a string variable to integer

if ageInt >= 18:
    print("Ticket value is fifteen dollars")
else:
    print("Ticket value is ten dollars")

    numOne = int(input("Type the number one: "))
    #   numIntOne = int(numOne)
    numTwo = int(input("Type the number two: "))
    #    numIntTwo = int(numTwo)

    if numOne > numTwo:
        print("The highest number is: ", str(numOne), ", ", "The lowest number is: ", str(numTwo), ". ")
    else:
        print("The highest number is: ", str(numTwo), ", ", "The lowest number is: ", str(numOne), ". ")

#   End of program.


