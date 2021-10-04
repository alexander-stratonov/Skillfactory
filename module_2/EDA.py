import numpy as np
import pandas as pd
arr1 = np.array([1,2,3,4])
print(arr1)
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
arr3 = np.array([5,6,7,8], dtype = float)
print(arr3)

df = pd.DataFrame()
x = df.values
print(type(x))

my_series = pd.Series([5, 6, 7, 8, 9, 10])
display(my_series.values)

display(np.empty(222)) # одномерный массив из пяти элементов, память для которого выделена, но не инициализирована
display(np.zeros((10, 7))) # массив размером 10x7, заполненный нулями 
display(np.ones((3,3,3))) # массив размером 3х3х3, заполненный единицами 
display(np.eye(3)) # единичная матрица (элементы главной диагонали равны 1, остальные — 0) размера 3х3
display(np.full((3, 5), 3.14))  # массив 3x5 заполненный числом 3.14
display(np.arange(0, 21, 7))  # одномерный массив, заполненный числами в диапазоне от 0 до 20 с шагом 7
display(np.linspace(0, 1, 5))  # массив из пяти чисел, равномерно распределённых в интервале между 0 и 1 включительно
display(np.random.randint(0, 10, (3, 3)))  # массив размера 3х3, заполненный случайными числами из диапазона от 0 до 9 (включительно)

my_secret = [x for x in range(1, 301, 7) if x%10 == 7 or x%10 == 1]
display(np.array([my_secret, [x/2 for x in my_secret], [x-100 for x in my_secret]]))

display(np.array([i for i in range(11) if i%2]))