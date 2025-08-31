"""
* Name         : abstractclass.py
* Author       : Matthew Stevens
* Created      : 7-5-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is Demonstrates abstract classes. The input is base class and subclasses the output is the details about each bicycle motorcycle and car.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or unmodified.
"""


from abc import ABC, abstractmethod

# base class
class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass


# Subclass
class Bicycle(Rider):
    def ride(self):
        return "Human powered, not enclosed"

    def riders(self):
        return "1 or 2 if tandem or a daredevil"


# Subclass
class Motorcycle(Rider):
    def ride(self):
        return "Engine powered, not enclosed"

    def riders(self):
        return "1 or 2"


# Subclass
class Car(Rider):
    def ride(self):
        return "Engine powered, enclosed"

    def riders(self):
        return "1 plus comfortably"


# Driver 
def main():
    bike = Bicycle()
    moto = Motorcycle()
    car = Car()

    print(bike.ride())
    print(bike.riders())
    print(moto.ride())
    print(moto.riders())
    print(car.ride())
    print(car.riders())


if __name__ == "__main__":
    main()
