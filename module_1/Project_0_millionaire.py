import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from IPython.display import display
data = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/movie_bd_v5.csv')
profit = data.revenue - data.budget
data['profit'] = profit
with pd.option_context('display.max_columns', None):
    display(data.sample(1))
answers = {}

print('ВОПРОС №1')
answers1 = data.sort_values('budget', ascending=False)
display(answers1)
answers['1'] = 'Pirates of the Caribbean: On Stranger Tides (tt1298650)'

print('ВОПРОС №2')
answers2 = data.sort_values('runtime', ascending=False)
display(answers2)
answers['2'] = 'Gods and Generals (tt0279111)'

print('ВОПРОС №3')
answers3 = data.sort_values('runtime', ascending=True)
display(answers3)
answers['3'] = 'Winnie the Pooh (tt1449283)'

print('ВОПРОС №4')
answers4 = data.runtime.mean()
display(answers4)
answers['4'] = '110'

print('ВОПРОС №5')
answers5 = data.runtime.describe()
display(answers5)
answers['5'] = '107'

print('ВОПРОС №6')
answers6 = data.sort_values('profit', ascending=False)
display(answers6)
answers['6'] = 'Avatar (tt0499549)'

print('ВОПРОС №7')
answers7 = data.sort_values('profit', ascending=True)
display(answers7)
answers['7'] = 'The Lone Ranger (tt1210819)'

print('ВОПРОС №8')
answers8 = data[data.revenue > data.budget]
display(answers8)
answers['8'] = '1478'

print('ВОПРОС №9')
answers9 = data[(data.release_year == 2008)].sort_values('profit', ascending=False)
display(answers9)
answers['9'] = 'The Dark Knight (tt0468569)'

print('ВОПРОС №10')
answers10 = data[(data.release_year >= 2012) &(data.release_year <= 2014)].sort_values('profit', ascending=True)
display(answers10)
answers['10'] = 'The Lone Ranger (tt1210819)'

print('ВОПРОС №11')
answers11 = pd.Series(data['genres'].str.cat(sep='|').split('|')).value_counts()[:5]
display(answers11)
answers['11'] = 'Drama'

print('ВОПРОС №12')
answers12 = data[data.profit > 0].copy()
answers12.genres = answers12.genres.str.split('|')
answers12 = answers12.genres.explode().value_counts()
display(answers12)
answers['12'] = 'Drama'

print('ВОПРОС №13')
answers13 = data.groupby('director').sum().sort_values('profit', ascending=False)
display(answers13)
answers['13'] = 'Peter Jackson'

print('ВОПРОС №14')
answers14 = data[data.genres.str.contains("Action")]
answers14 = answers14['director'].str.cat(sep='|') 
answers14 = pd.Series(answers14.split('|')).value_counts(ascending=False) 
display(answers14)
answers['14'] = 'Robert Rodriguez'

print('ВОПРОС №15')
answers15 = data.copy()
answers15.cast = data.cast.apply(lambda x: str(x).split('|'))
answers15 = answers15.explode('cast')
answers15 = answers15[answers15.release_year == 2012].groupby('cast').revenue.sum().sort_values(ascending=False)
display(answers15)
answers['15'] = 'Chris Hemsworth'

print('ВОПРОС №16')
answers16 = pd.Series(data[data.budget > data.budget.mean()].cast.str.split('|').sum()).value_counts() 
display(answers16)
answers['16'] = 'Matt Damon'

print('ВОПРОС №17')
answers17 = data[data.cast.str.contains("Nicolas Cage")].genres.str.split('|').explode().value_counts() 
display(answers17)
answers['17'] = 'Action'

#display(answers)






























































