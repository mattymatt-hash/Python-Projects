"""
* Name         : basiclooping.py
* Author       : Matthew Stevens
* Created      : 6-9-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to demonstrate basic for loop use in python
 print floating point number list
 print odd integars descending from 99-55
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

def print_float_numbers(float_numbers):
    """
    Print floating point number from list.

    Args:
        float numbers to display.
    """
    print("floating point numbers")
    for num in float_numbers:
        print(num)


def print_descending_odds(start, end):
    """
    Print odd integers in descending order from start to end.
    Args:
        start (int) The starting number 
        end (int) The ending number 
    """
    print(f"\nodd integers descending from {start}-{end}")
    for i in range(start, end - 1, -1):
        if i % 2 != 0:
            print(i)

