import pandas as pd
from IPython.display import display
#df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/data_sf.csv')

a = df[df.Nationality == 'Spain'].Wage.value_counts(bins = 4,normalize=True)
display('1',a)

b = df[df.Club == 'Manchester United'].Nationality.value_counts()
display('2',len(b))

c = df[(df.Club == 'Juventus') & (df.Nationality  == 'Brazil')]
display('3',c.Name)

d = df[df.Age > 35].Club.value_counts()
display('4',d.head(5))

e = df[df.Nationality == 'Argentina'].Age.value_counts(bins = 4)
display('5',e)

f = df[(df.Age == 21) & (df.Nationality  == 'Spain')]
f1 = df[df.Nationality  == 'Spain']
f2 = round((len(f) / (len(f1) / 100)), 2)
display('6',f2)