"""
* Name         : Compound Expressions Assignment

* Author       : Matthew Stevens
* Created      : 6-1-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to practice with Compound Expressions. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

MAX = 20
MIN = 1

# y variable value
y = 25

# is y above MAX
if y > MAX:
    print("y is above MAX")

# is y below MIN
if y < MIN:
    print("y is below MIN")

# value of x
x = 10

# is x between min and max but not equal
if MIN < x < MAX:
    print("x is between MIN and MAX (excluding both)")


if MIN <= x < MAX:
    print("x is within MIN up to MAX (excluding MAX)")


if MIN < x <= MAX:
    print("x is above MIN up to and including MAX")