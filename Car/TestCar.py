# Import Car class from Car file
from Car import Car

# Create a class named TestCar
class TestCar:
    def Test_car(self):
# Create a car object
     car = Car(2023, "Honda", 0)

# Accelerate
   # First call
     car.accelerate()
     print(car.get_speed())
    
    # Second call
     car.accelerate()
     print(car.get_speed())

    # Third call
     car.accelerate()
     print(car.get_speed())

    # Fourth call
     car.accelerate()
     print(car.get_speed())

    # Fifth call
     car.accelerate()
     print(car.get_speed())   

# Brake
# Print the result

run = TestCar()
run.Test_car()