# Kenneth John Costa
# Activity Pet

# Create a Pet class
class Pet:

# Create a constructor for Pet class
    def __init__ (self, name, type, age):

# Create a private instance variable
     self.__name = name
     self.__type = type
     self.__age = age

# Get the name of the pet
    def get_name(self):
        return self.__name
        
# Set the name of the pet
    def set_name(self, name):
        self.__name = name 

# Get the animal type of the pet
    def get_type(self):
        return self.__type
    
# Set the animal type of the pet
    def set_type(self, type):
        self.__type = type

# Get the age of the pet
    def get_age(self):
        return self.__age
    
# Set the age of the pet
    def set_age(self, age):
        self.__age = age