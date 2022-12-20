#universal function
import numpy as np

my_number1 = np.array([1,4,5,15,24,22])
my_number_sqrt1 = np.sqrt(my_number1)

my_number2 = np.arange(1,7)*10

result = np.add(my_number_sqrt1,my_number2)

print(result)
