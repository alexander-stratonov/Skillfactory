import pandas as pd
from IPython.display import display
df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
#df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/data_sf.csv')
#small_df = df[df.columns[1:8]].head(25)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(small_df)
a = df[(df.Club == 'Chelsea')].Wage.sum()
a1 = df.groupby(['Club'])['Wage'].sum()['Chelsea']
display(a)
display(a1)

b = df[(df.Nationality == 'Argentina') & (df.Age == 20)].Wage.max()
display(b)

c = df[(df.Nationality == 'Argentina') & (df.Age == 30)].Wage.max()
display(c)

d = df[(df.Nationality == 'Argentina') & (df.Age == 30)].Wage.min()
display(d)

e = df[(df.Nationality == 'Argentina') & (df.Club == 'FC Barcelona')].Strength.max()
e1 = df[(df.Nationality == 'Argentina') & (df.Club == 'FC Barcelona')].Balance.max()
display(e)
display(e1)