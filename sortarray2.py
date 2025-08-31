"""
* Name         : program name   Search and Sort Array 
* Author       : Matthew Stevens
* Created      : Creation Date 6-22
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is search for the array The input is the hardcoded array The output is the sorted arrays results
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""


import array  


def sort_array(arr):
    """Sorts the array """
    arr[:] = array.array(arr.typecode, sorted(arr))  
  

def search_array(arr, target):
    """Searches for array and returns index or -1"""
    try:
        return arr.index(target)  
    except ValueError:
        return -1 


def main():
   
    data = array.array('i', [8, 6, 7, 5, 3, 0, 9])  # like the song

    print("Original array:", data.tolist())  

    sort_array(data) 
    print("Sorted array:  ", data.tolist()) 

    target = 25  
    index = search_array(data, target)  

   
    if index != -1:
        print(f"Value {target} found  {index}.") 
    else:
        print(f"Value {target} not found") 


if __name__ == "__main__":
    main()

# no return statement for sort_array() because you can change its value inside a function and those changes will extend outside of that functiom