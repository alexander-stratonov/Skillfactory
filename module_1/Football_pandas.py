import pandas as pd
from IPython.display import display
df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
#df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/data_sf.csv')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df)
pivot = df.loc[df['Club'].isin(['FC Barcelona',
                                'Real Madrid',
                                'Juventus',
                                'Manchester United'])
               ].pivot_table(values=['Wage'],
index=['Nationality'],
columns=['Club'],
aggfunc='sum',
margins=True,
fill_value=0)
display(pivot)
#df2 = df.pivot_table(columns = 'Position', index = 'Club', values = 'Wage', aggfunc = 'max')
#display(df2)
pivot = df.loc[df['Club'].isin(['FC Barcelona',
                                'Real Madrid',
                                'Juventus',
                                'Manchester United'])
               ].pivot_table(values=['Name'],
index=['Nationality'],
columns=['Club'],
aggfunc='count',
margins=True,
fill_value=0)
display(pivot)