#deep copies
import numpy as np

numbers_1 = np.arange(1,6)

numbers_2  = numbers_1.copy() #use .copy for deep copies

print(numbers_2)
