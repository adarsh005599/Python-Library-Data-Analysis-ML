# Numpy problem solving file🤯😁

import  numpy as np
import matplotlib.pyplot as plt

Swiggy_Booking = np.array(
    [
    [1,1000,2000,3000,4000], #1st
    [2,1002,2002,3002,4002], #2nd
    [3,1003,2003,3003,4003], #3rd
    [4,1004,2004,3004,4004], #4th
    [5,1005,2005,3005,4005], #5th
    ]
)

print("===Swiggy Active orders===")
print(Swiggy_Booking.shape)
print(Swiggy_Booking.size)
print("\n Order details of the first 3: \n", Swiggy_Booking[:3])