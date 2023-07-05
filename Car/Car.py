# Kenneth John Costa
# Activity Car

# Create a Car class
class Car:

# Create a constructor for Car class
    def __init__(self, year, make, speed = 0):
        
# Create a private instance variable
        self.__year = year
        self.__make = make
        self.__speed = speed

# Get the year of Car
    def get_year(self):
        return self.__year
    
# Set the year of Car
    def set_year(self, year):
        self.__year = year

# Get the make of Car
    def get_make(self):
        return self.__make
    
# Set the make of Car
    def set_make(self, make):
        self.__make = make
        
# Create a get speed method
# Set the speed of Car
# Create an accelerate method
# Create a brake method