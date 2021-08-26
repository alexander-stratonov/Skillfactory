import pandas as pd
from IPython.display import display
#df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/data_sf.csv')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df)
pivot = df.pivot_table(values='Name',
index='Club',
columns='Position',
aggfunc='count',
fill_value=0)
display(pivot)
#1
s = round(pivot['GK'].mean(),3)
display(s)
#2
a = (pivot['CM'].value_counts())
display(a)