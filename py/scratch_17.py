"""
How Much You Have software
Author: Leonardo Miguel
Date: 13/02/2022
Description:
    The software has the proposal to validate
how much money you have and do a calculation
showing for user what he can do without having to much
money or having to much.
Tools: Pycharm & w3Schools
"""

# Declarations

# The user needs to type how much money he has.
validate_money = float(input("How much money you have? Type here: "))

# Conditionals

# This validates user if he has 0 to 29 dollars.
if validate_money <= 29:
    print("Stay at home and watch some TV Shows.")
    input("Press enter to shutdown...")

# This validates user if he has 30 or 49 dollars.
elif validate_money == 30 or validate_money <= 49:
    print("Go at the cinema and watch some movies. ")
    input("Press enter to shutdown...")

# This validates user if he has 50 or more dollars.
else:
    print("Go diner off home. ")
    input("Press enter to shutdown...")

    # end
