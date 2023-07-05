# Import Fan class from Fan file
from Fan import Fan

def Test_Fan():
    
# Fan1
     Fan1 = Fan(Fan.FAST, True, 10, "Yellow")

# Print the result of Fan1
     print("\033[92m=" * 50)
     print("\033[95m\033[1mFAN 1".center(58))
     print("\033[92m=" * 50)

     print("\033[93mSPEED:", Fan1.get_speed())
     print("\033[93mSWITCH:", Fan1.get_switch())
     print("\033[93mRADIUS:", Fan1.get_radius())
     print("\033[93mCOLOR:", Fan1.get_color())
     
     print("\033[92m=" * 50)
     print()
     print("\033[92m=" * 50)

     print()
     print()
     print()

# Fan2
     Fan2 = Fan(Fan.MEDIUM, False, 5, "Blue")

# Print the result of Fan2
     print("\033[92m=" * 50)
     print("\033[95m\033[1mFAN 2".center(58))
     print("\033[92m=" * 50)

     print("\033[96mSPEED:", Fan2.get_speed())
     print("\033[96mSWITCH:", Fan2.get_switch())
     print("\033[96mRADIUS:", Fan2.get_radius())
     print("\033[96mCOLOR:", Fan2.get_color())

     print("\033[92m=" * 50)
     print()
     print("\033[92m=" * 50)


Test_Fan()