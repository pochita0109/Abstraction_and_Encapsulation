# Import Pet class from Pet file
from Pet import Pet

# Create a class name TestPet
class TestPet:
    def test_pet():

# Ask the user to enter the name of pet
        name = input("Please enter the name of your pet: ")

# Ask the user to enter the type of pet
        type = input("Please enter what kind of animal is your pet: ")

# Ask the user to enter the age of pet
        age = input("Please enter the age of your pet in years: ")

# Create pet object
        pet = Pet(name, type, age)

# Print the result
        print(pet.get_name())
        print(pet.get_type())
        print(pet.get_age())

run = TestPet
run.test_pet()