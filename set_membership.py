"""
* Name         : program name   set assignment
* Author       : Matthew Stevens
* Created      : Creation Date 6-19-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to test a set of values that we input...  The input is first is apples and 2nd is 5... The output is first is The value 'apple' in the set {'banana', 'apple', 'cherry'} then the second output is The value '5' not in the set {'banana', 'apple', 'cherry'}
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
def in_set(input_set, value):
    return value in input_set  #if value is there then true if not then false

def main():
    test_set = {'banana', 'apple', 'cherry'}       #this is the test set
   
   # Test 1
    test_value = 'apple'                          #this is one value we are testing
    result = in_set(test_set, test_value)
    if result:
        print(f"The value '{test_value}' in the set {test_set}")
    else:
        print(f"The value '{test_value}' not in the set {test_set}")
    
    # Test 2
    test_value = 5                                 #this is the second value we are testing
    result = in_set(test_set, test_value)
    if result:
        print(f"The value '{test_value}' in the set {test_set}")
    else:
        print(f"The value '{test_value}' not in the set {test_set}")

# main 
if __name__ == "__main__":
    main()