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

#5
my_sin = np.sin(my_array)
display(round(sum(sum(my_sin)),3))

#6
my_sin[1:4,1:4]=1
display(round(sum(sum(my_sin)),3))

#7
a = my_sin[:,0:4]
a = a.reshape(10,2)
display(round(sum(a[:,0]),3))


bigdata = np.array([x*x for x in range(101, 1000, 2)])
#8
display(np.median(bigdata))
#9
display(round(np.std(bigdata)))
#10
display(np.corrcoef(bigdata[::2], bigdata[1::2]))

