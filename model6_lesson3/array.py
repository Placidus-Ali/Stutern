from array import array
import numpy as np
                  
# Generate an array of numbers between 1 and 100 with both numbers included
my_array = np.arange(1,101)
print(my_array)

# get the even numbers
even_numbers = my_array[1:100:2]
print(even_numbers)

# find the LCM of the even numbers
lcm = np.lcm.reduce(even_numbers)
print(lcm)
