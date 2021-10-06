import numpy as np
from IPython.display import display

#2
display(np.ones((5,10), dtype = int))

#4
my_array = np.array([[1,2,3,4,5],
                     [6,7,8,9,10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]])
display(my_array[1:4,1:4])
