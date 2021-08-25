import pandas as pd
from IPython.display import display
df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')

a = df[df.Nationality == 'Spain'].Wage.value_counts(bins = 4)
display(a)

b = df[df.Club == 'Manchester United'].Nationality.value_counts()
display(len(b))

c = df[(df.Club == 'Juventus') & (df.Nationality  == 'Brazil')]
display(c.Name)

d = df[df.Age > 35].Club.value_counts()
display(d)

e = df[df.Nationality == 'Argentina'].Age.value_counts(bins = 4)
display(e)

f = df[(df.Age == 21) & (df.Nationality  == 'Spain')]
f1 = df[df.Nationality  == 'Spain']
f2 = round((len(f) / (len(f1) / 100)), 2)
display(f2)