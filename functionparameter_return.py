"""
* Name         : Function Parameter and Return Value Assignment
* Author       : Matthew Stevens
* Created      : 6-8-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : a function named get_area which takes a single radius parameter and returns the calculated area as a float.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
def get_area(radius):
    
    """ Calculate and return a circles area
parameters:radius (int or float): The radius of the circle.
returns:float the area of the circle or -1 if the input isnt a num."""
    
    try:
        radius = float(radius)
        if radius < 0:
         return -1
        pi = 3.141592653589793
        area = pi * radius ** 2
        return area
    except (ValueError, TypeError):
        return -1

if __name__ == "__main__":
    user_input = input("enter radius: ")
    result = get_area(user_input)
    if result == -1:
        print("wrong input radius.")
    else:
        print(f"area of the circle: {result:.2f}")