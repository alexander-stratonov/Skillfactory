import numpy as np
import pandas as pd
from IPython.display import display

a = np.array([3,6,9])
b = np.array([12,15,18])
result1 = a+b
result2 = b-a
result3 = a*b
result4 = a/b
result5 = a*2
print('Сумма: {}\nРазность: {}\nПроизведение: {}\nЧастное: {}\nУмножение на число: {}'.format(result1, result2, result3, result4, result5))

my_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
display(my_array)
display(my_array.T)

my_array = np.random.randint(0, 10, 20)
display(my_array)
display(my_array.reshape((4,5)))

my_array = np.array([[1,2,3], [11,22,33], [111,222,333]])
display(my_array)
display(my_array.flatten())

my_array = np.random.randint(0, 10, (3,4))
display(my_array)
display(my_array<5)
display(my_array[my_array<5])
mask = np.array([1, 0, 1, 0], dtype=bool)
display(my_array[:, mask])

my_array = np.random.randint(0, 10, (4, 6))
display(my_array)
display(np.sort(my_array, axis=1))
display(np.sort(my_array, axis=0))
#1
first = [x**(1/2) for x in range(100)]
second = [x**(1/3) for x in range(100, 200)]
third = [x/y for x in range(200,300,2) for y in [3,5]]
great_secret = np.array([first, second, third]).T
display(great_secret)
#2
a=np.cos(great_secret[0, :])
a1=a[0]+a[1]+a[2]
display(round(a1, 2))
#3
display(sum(great_secret[great_secret>50]))
#4
display(great_secret.flatten()[150])