"""
* Name         : program name Dictionary Update Assignment
* Author       : Matthew Stevens
* Created      : Creation Date 6-20
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to create and update a dictionary... The input is a name from the user for a new entry... The output is the complete listing of the new updated phonebook.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""



def main():
    """
    Create a phone book for the names and numbers in the given lists.
    The follow the instructions in the comments. 
    """

    names = ["juan", "michael", "steve", "jimmy", "tony", "merle", "willie"]

    numbers = ["708-555-9878", "630-555-0009", "630-555-1112", "515-555-9999", 
               "847-555-4443", "312-555-9823", "414-555-6767"]
    

    # --------------------------------------------------------------------------
    # TODO: Create an empty dictionary. Iterate over names and numbers, 
    # creating a dictionary that maps names to numbers. 
    # Hint: Look into to using thew zip function to iterate over names 
    # and numbers as a list of 2-tuples.
    #---------------------------------------------------------------------------
    phone_book = dict(zip(names, numbers))

     #---------------------------------------------------------------------------
    # TODO: Prompt user for a name NOT in your dictionary (continue to prompt 
    # user until they enter a name not already in the dictionary). Once a new 
    # name is provided, prompt for a phone number. Then add the key-value pair 
    # to your dictionary.
    #---------------------------------------------------------------------------
    while True:
        new_name = input("Enter a new name (not already in the phone book): ").strip().lower()
        if new_name not in phone_book:
            break
        print(f"'{new_name}' is already in the phone book. Please try again.")

    new_number = input(f"Enter a phone number for {new_name}: ").strip()
    phone_book[new_name] = new_number

     #---------------------------------------------------------------------------
    # TODO: Prompt user for a name in your dictionary (continue to prompt 
    # user until they enter a name already in the dictionary). Once an existing
    # name is provided, prompt for a new phone number, and update the dict
    # with the new number. 
    #-------------------------------------------------------------------------
    while True:
        existing_name = input("Enter an existing name in the phone book to update: ").strip().lower()
        if existing_name in phone_book:
            break
        print(f"'{existing_name}' is not in the phone book. Please try again.")

    updated_number = input(f"Enter the new phone number for {existing_name}: ").strip()
    phone_book[existing_name] = updated_number

     #---------------------------------------------------------------------------
    # TODO: Print dictionary with new name/number and updated number. 
    # --------------------------------------------------------------------------
    print(f"\nUpdated Phone Book ({len(phone_book)} entries):")
    for name, number in phone_book.items():
        print(f"{name}: {number}")   

if __name__ == "__main__":
    main()
