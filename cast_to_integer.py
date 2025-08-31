"""
Program: cast_to_integer.py
Author: Matthew Stevens
Last date modified: 5/24/2025

The purpose of this program is to accept any input, 
convert to a integer type and output the integer. 
"""
Your_numbers = input("Enter a value")

#just a little trycatch block
try:
    integer_value = int(float(Your_numbers))
except ValueError:
    integer_value = "Error: Wrong."

print("Result:", integer_value)
#reminder and integer is a whole number without a decimal point or fraction. just a whole number