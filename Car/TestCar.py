# Import Car class from Car file
from Car import Car

# Create a class named TestCar
class TestCar:
    def Test_car(self):
# Create a car object
     car = Car(2023, "Honda", 0)

# Print the result
     print("\033[92mYEAR:", car.get_year())
     print("\033[92mMODEL:", car.get_make())
     print("\033[92mSPEED:", car.get_speed())

     print()

# Accelerate
     print("\033[93mAccelerating....")
    # First call
     car.accelerate()
     print("\033[93mCurrent Speed:", car.get_speed())
    
    # Second call
     car.accelerate()
     print("\033[93mCurrent Speed:", car.get_speed())

    # Third call
     car.accelerate()
     print("\033[93mCurrent Speed:", car.get_speed())

    # Fourth call
     car.accelerate()
     print("\033[93mCurrent Speed:", car.get_speed())

    # Fifth call
     car.accelerate()
     print("\033[93mCurrent Speed:", car.get_speed())   
     
     print()

# Brake
     print("\033[91mDeccelerating....")
    # First call
     car.brake()
     print("\033[91mCurrent Speed:", car.get_speed())

     # Second call
     car.brake()
     print("\033[91mCurrent Speed:", car.get_speed())

     # Third call
     car.brake()
     print("\033[91mCurrent Speed:", car.get_speed())

     # Fourth call
     car.brake()
     print("\033[91mCurrent Speed:", car.get_speed())

     # Fifth call
     car.brake()
     print("\033[91mCurrent Speed:", car.get_speed())

run = TestCar()
run.Test_car()