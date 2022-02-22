"""
Calculating Apples (or any other fruit) software
Author: Leonardo Miguel
Date: 13/02/2022
Description:
    This software has the proposal to do an app
that can calculate any fruit and show for user what's
the final result.
    For example if the user types:
    6 apples
    This value will be saved and then a calculation will
run, then the result will appear for user.

Tools: Pycharm & w3schools

"""

# Declarations

apples = int(input("Type a total of apples you wanna buy: "))
calculate_apples = apples * 0.30
calculate_apples_two = apples * 0.25
calculate_apples_three = apples * 0.20
calculate_apples_four = apples * 0.15

# Conditionals

# Here we are at the validations of our software.


if apples < 12:
    # Validation to lowest or equal of 6 apples
    print(round(calculate_apples, 2))
    input("Press Enter to shutdown...")
elif apples >= 12 and apples < 20:
    # Validation to higher or equal 12 apples, and lowest or equal 20
    print(round(calculate_apples_two, 2))
    input("Press Enter to shutdown...")
elif apples >= 20 and apples <= 24:
    # Validation to apples higher of 19 to 24 apples
    print(round(calculate_apples_three, 2))
    input("Press Enter to shutdown...")
else:
    print(round(calculate_apples_four, 2))
    input("Press Enter to shutdown...")
# End

