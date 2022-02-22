"""
Order by reverse software
Author: Leonardo Miguel
Date 13/02/2022
Description:
    This app has the proposal to make the numbers
appear in a reverse row list.
Ex:
1,2,3 to 3,2,1
Tools: PyCharm and w3Schools
"""

ohLookDecNumbers = []


for i in range(3):
    i = int(input(f"Type the number {i+1}: "))
    ohLookDecNumbers.append(i)

ohLookDecNumbers.reverse()

print(ohLookDecNumbers)
input("Press enter to shutdown")

# End


