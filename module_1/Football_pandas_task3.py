import pandas as pd
from IPython.display import display
df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
#df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/data_sf.csv')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df)
#1
s = df[(df.Nationality == 'Russia') & 
     (df.Club == "AS Monaco")].Wage.value_counts()
display(s)
#2
s1 = df.pivot_table(values = ['SprintSpeed'],
              index = ['Club'],
              columns = ['Position'],
              aggfunc = 'mean',
              fill_value=0)
s1 = s1['SprintSpeed']
display(s1.max().sort_values(ascending=False).head(5))
#3
s2 = df.loc[df['Position'].isin(['RB','LM', 'RM','CF', 'RWM', 'RS','ST'])
             ].pivot_table(values='SprintSpeed',index=['Club'],
columns=['Position'],
aggfunc='mean')
display(s2['ST'].sort_values(ascending=False).head(5))

