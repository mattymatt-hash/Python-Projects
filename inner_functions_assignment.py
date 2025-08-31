"""
* Name         : program name inner functions
* Author       : Matthew Stevens
* Created      : Creation Date6-14
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : the purpose of this program is to calculaye the area and perimeter of a rectangle or saquare  input is the shapes side length and width and output is the shapes perimeter and area roundede to two decimal places
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
def measurements(dimensions):
    """Returns the perimeter and area for a rectangle or square based on list dimensions."""

    def area(a_list):
        if len(a_list) == 1:
            return a_list[0] ** 2  # square
        elif len(a_list) == 2:
            return a_list[0] * a_list[1]  # rectangle
        else:
            return 0  # invalid

    def perimeter(a_list):
        if len(a_list) == 1:
            return 4 * a_list[0]  # square
        elif len(a_list) == 2:
            return 2 * (a_list[0] + a_list[1])  # rectangle
        else:
            return 0  # invalid

    shape_area = area(dimensions)
    shape_perimeter = perimeter(dimensions)
    return f"Perimeter = {shape_perimeter:.2f} Area = {shape_area:.2f}"


def main():
    # Test with a rectangle: 2.5 x 3.07
    rectangle_result = measurements([2.5, 3.07])
    print("Rectangle:", rectangle_result)

    # Test with a square: side length 4.2
    square_result = measurements([4.2])
    print("Square:", square_result)


if __name__ == "__main__":
    main()