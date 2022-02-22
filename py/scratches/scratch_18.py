"""
Higher or Lowest? Software
Date: 13/02/2022
Author: Leonardo Miguel
Description:
    This app has the proposal to validate a number that
user type and show for him which category this number is.
Tools: Pycharm & w3Schools
"""

# Declarations

validate_number = (int(input("Type a number to see which category he is: ")))

if validate_number <= 10:
    print("This number are in 0 to 10 category")
elif validate_number <= 20:
    print("This number are in 20 to 30 category")
else:
    print("This number are higher than 30 or are 30")


# end
