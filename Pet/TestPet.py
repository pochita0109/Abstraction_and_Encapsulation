# Import Pet class from Pet file
from Pet import Pet

# Create a class name TestPet
class TestPet:
    def test_pet():

# Ask the user to enter the name of pet
        name = input("\033[92mPlease enter the name of your pet: ")

# Ask the user to enter the type of pet
        type = input("\033[92mPlease enter what kind of animal is your pet: ")

# Ask the user to enter the age of pet
        age = input("\033[92mPlease enter the age of your pet in years: ")

# Create pet object
        pet = Pet(name, type, age)

# Print the result
        print()
        print("\033[91m=" * 50)
        print("\033[95m\033[1mYOUR PET INFORMATION".center(58))
        print("\033[91m=" * 50)
        print()

        print("\033[93mPet Name:", pet.get_name())
        print("\033[93mType:", pet.get_type())
        print("\033[93mAge:", pet.get_age())

        print()
        print("\033[91m=" * 50)
        print("\033[91m=" * 50)
        print()
        
run = TestPet
run.test_pet()