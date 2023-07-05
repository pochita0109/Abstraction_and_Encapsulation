# Import Fan class from Fan file
from Fan import Fan

def Test_Fan():

# Fan1
     Fan1 = Fan(Fan.FAST, True, 10, "Yellow")

# Print the result of Fan1
     print(Fan1.get_speed())
     print(Fan1.get_switch())
     print(Fan1.get_radius())
     print(Fan1.get_color())

# Fan2
     Fan2 = Fan(Fan.MEDIUM, False, 5, "Blue")

# Print the result of Fan2
     print(Fan2.get_speed())
     print(Fan2.get_switch())
     print(Fan2.get_radius())
     print(Fan2.get_color())

Test_Fan()