
"""
* Name         : program name composition.py
* Author       : Matthew Stevens
* Created      : Creation Date 7-2
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to create a computer class that uses 2 other classes internally. The input is the computer names list. The output is the printed statements. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
import random
from datetime import datetime

# Do not modify.
class Memory:
    """
    Class representation of computer memory.
    """
    def __init__(self):

        self.total_ram_gb = 16

    def available(self):
        in_use = random.uniform(0, self.total_ram_gb)
        avail = self.total_ram_gb - in_use 
        return avail


# Do not modify.
class DiskSpace:
    """
    Class representation of computer hard disk storage.
    """
    def __init__(self):
        self.total_capacity_gb = 512

    def available(self):
        in_use = random.uniform(0, self.total_capacity_gb)
        avail = self.total_capacity_gb - in_use 
        return avail



class Computer:
    """
    Computer class. 
    
    Attributes:
        name: str
            Passed in as an argument to the constructor. 

    Methods: 
        get_info:
            Returns a string of the form:

            [timestamp] computer name: <name>, available memory: <available memory>, available storage: <available storage>
    
    """

    # Remove pass after you add your code.

    def __init__(me, name):
        me.name = name
        me.memory = Memory()
        me.disk = DiskSpace()
   
    def get_info(me):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        available_memory = round(me.memory.available(), 2)
        available_storage = round(me.disk.available(), 2)

        print(f"{timestamp}: computer name: {me.name}, available memory: {available_memory} GB, available storage: {available_storage} GB")




def main():


    machine_names = ["RQS445", "MIKES-MACHINE", "Leet-315"]

    # For each of the machine_names, create an instance of the Computer
    # class, then call `get_info` for each. 

    for name in machine_names:
        comp = Computer(name)
        comp.get_info()

if __name__ == "__main__":
    main()