"""
* Name         : program name  Encapsulation Assignment
* Author       : Matthew Stevens
* Created      : Creation Date 6-30
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to store a employees data in a class.The input is the employees name and 4 attributes.  The output is the formatted data
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
class Employee:
    """
    Employee class 4 more attributes in constructor and body
    """
    def __init__(self, last_name, first_name, address, phone_number, salary, start_date):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.salary = salary
        self.start_date = start_date

def display(self):
         """
        Display employee information 
        in desired format
         """
         return (
            f"LAST_NAME, FIRST_NAME: {self.last_name}, {self.first_name}\n"
            f"PHONE_NUMBER: {self.phone_number}\n"
            f"ADDRESS: {self.address}\n"
            f"START DATE: {self.start_date}\n"
            f"SALARY: {self.salary}"
        )
        # Remove pass after you add your code.

        

    




def main():

    person_list = [
        {"last_name": "VanRossum", "first_name": "Guido","address": "461 Ocean Blvd",
        "phone_number": "773-735-1849", "salary": 97500, "start_date": "1991-02-22"},

        {"last_name": "Haggard", "first_name": "Merle","address": "Bakersfield, CA",
        "phone_number": "484-765-2231", "salary": 72500, "start_date": "1967-11-08"},

        {"last_name": "Prine", "first_name": "John","address": "Paradise, KY",
        "phone_number": "743-435-8310", "salary": 88500, "start_date": "1995-07-31"},
        ]
    
    # Iterate over person_list, and create a new Employee instance and call the 
    # display method for each.

    for person in person_list:
        emp = Employee(
            person["last_name"],
            person["first_name"],
            person["address"],
            person["phone_number"],
            person["salary"],
            person["start_date"]
        )
        
        print() 








if __name__ == "__main__":

    main()

