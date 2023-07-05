# Kenneth John Costa
# Activity Fan

# Create a Fan class
class Fan:

# Create constants for slow, medium, and fast
    SLOW = 1
    MEDIUM = 2
    FAST = 3

# Create a constructor for Fan class
    def __init__(self, speed = SLOW, on = False, radius = 5, color = "blue"):
     
# Create a private instance variable 
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

# Create an accessor (Getter) for speed
    def get_speed(self):
        return self.__speed
    
# Create a mutator (Setter) for speed
    def set_speed(self, speed):
        self.__speed = speed

# Create an accessor (Getter) for switch
    def get_switch(self):
        if self.__on == True:
            return "ON"
        else:
            return "OFF"

# Create a mutator (Setter) for switch
    def set_switch(self, on):
        self.__on = on
    
# Create an accessor (Getter) for radius
    def get_radius(self):
        return self.__radius
    
# Create a mutator (Setter) for radius
    def set_radius(self, radius):
        self.__radius = radius

# Create an accessor (Getter) for color
    def get_color(self):
        return self.__color
    
# Create a mutator (Setter) for color
    def set_color(self, color):
        self.__color = color