import numpy as np
from IPython.display import display

students = np.fromfile('C:/Users/user/Documents/GitHub/Skillfactory_Alexander_Stratoonv/module_2/students.txt', sep='\t').reshape(-1,4)
display(students)
mean = np.mean(students[:,-1])
display(mean)
median = np.median(students[:,-1])
display(median)

#1
a = np.median(students[:,2])
display(median)
#2
b = np.median(students[:,2]) - np.mean(students[:,2])
display(b)
#3
corr = np.corrcoef(students[:,1], students[:,2])
display(corr)
corr = np.corrcoef(students[:,1], students[:,3])
display(corr)
corr = np.corrcoef(students[:,2], students[:,3])
display(corr)
#4
std = np.std(students[:,-1])
display(std)
#5
display(np.var(students[:,2]))
