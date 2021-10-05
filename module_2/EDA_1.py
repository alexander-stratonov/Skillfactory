import numpy as np
import pandas as pd
from IPython.display import display

np.set_printoptions(precision=4,suppress=True)
first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]
big_secret = np.array([first_line, second_line, third_line, second_line, first_line])
display(big_secret)

#1
a = big_secret[:,-1]
a1 = a[0]+a[1]+a[2]+a[3]+a[4]
print('1 =', a1)
#2
b= big_secret[:,0:5]
b2 = 0
for x in range(0,5):
    j = b[x,x]
    b2 = b2 + j
print('2 =', b2)
#3
c= big_secret[:,-5:]
c2 = 1
for x in range(0,5):
    j = c[x,x]
    c2 = c2 * j
print('3 =', c2)

#_
my_array = np.random.randint(1, 100, (4, 6)) 
display(my_array)
my_slice = my_array[1:3, 2:4]
display(my_slice)
my_slice[:] = 0
display(my_array)

#_
big_secret[::2,::2] = -1
big_secret[1::2, 1::2] = 1
display(big_secret)

#4
d= big_secret[:,0:5]
d2 = 0
for x in range(0,5):
    j = d[x,x]
    d2 = d2 + j
print('4 =', d2)

#5
e= big_secret[:,-5:]
e2 = 1
for x in range(0,5):
    j = c[x,x]
    e2 = e2 * j
print('5 =', e2)