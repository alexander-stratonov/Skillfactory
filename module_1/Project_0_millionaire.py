import pandas as pd
from collections import Counter
from IPython.display import display
from itertools import combinations
data = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/movie_bd_v5.csv')
#data = pd.read_csv('C:/Users/user/Documents/GitHub/Skillfactory_Alexander_Stratoonv/module_1/movie_bd_v5.csv')
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
answers11 = pd.Series(data['genres'].str.cat(sep='|').split('|')).value_counts()
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

print('ВОПРОС №18')
answers18 = data[data['production_companies'].str.contains('Paramount Pictures')]
answers18 = answers18[['profit', 'original_title', 'imdb_id']].sort_values('profit', ascending=False)
display(answers18)
answers['18'] = 'K-19: The Widowmaker (tt0267626)'

print('ВОПРОС №19')
answers19 = data.groupby(data['release_year'])['revenue'].sum().sort_values(ascending=False)
display(answers19)
answers['19'] = '2015'

print('ВОПРОС №20')
answers20 = data[data.production_companies.str.contains("Warner Bros", na=False)].groupby(
    data['release_year'])['profit'].sum().sort_values(ascending=False)
display(answers20)
answers['20'] = '2014'

print('ВОПРОС №21')
answers21 = data.release_date.str.split('/').apply(lambda x: x[0]).value_counts()
display(answers21.sort_values(ascending=False))
answers['21'] = 'Сентябрь'

print('ВОПРОС №22')
answers22 = data.release_date.str.split('/').apply(lambda x: x[0]).value_counts()
display(answers22[['6','7','8']].sum())
answers['22'] = '450'

print('ВОПРОС №23')
answers23 = data.copy()
answers23['mouth'] = pd.DatetimeIndex(answers23['release_date']).month
answers23['directors'] = answers23.director.str.split('|')
answers23 = answers23.explode('directors')
answers23 = answers23[(answers23['mouth'] == 1) | (answers23['mouth'] == 2) | (answers23['mouth'] == 12)].value_counts(subset='directors')
answers23 = answers23.idxmax()
display(answers23)
answers['23'] = 'Peter Jackson '

print('ВОПРОС №24')
answers24 = data.copy()
answers24['production_companies'] = answers24['production_companies'].str.split('|')
answers24 = answers24.explode('production_companies')
answers24['title_length'] = answers24.original_title.apply(lambda x: len(x))
answers24 = answers24.groupby('production_companies').title_length.mean().sort_values(ascending = False)
display(answers24)
answers['24'] = 'Four By Two Productions'

print('ВОПРОС №25')
answers25 = data.copy()
answers25['production_companies'] = answers25['production_companies'].str.split('|')
answers25['overview'] = answers25['overview'].str.split(' ')
answers25 = answers25.explode('production_companies')
answers25['overview'] = answers25.overview.apply(lambda x: len(x))
answers25 = answers25.groupby('production_companies').overview.mean().sort_values(ascending = False)
display(answers25)
answers['25'] = 'Midnight Picture Show '

print('ВОПРОС №26')
answers26 = data[data['vote_average'] >= 7.9][['original_title', 'vote_average']]
display(answers26)
answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave'

print('ВОПРОС №27')
answers27 = data.copy()
answers27['cast_split'] = answers27['cast'].str.split('|')
answers27['cast_togever'] = answers27.cast_split.apply(lambda x: list(combinations(x, 2)))
answers27 = Counter(answers27['cast_togever'].sum()).most_common(1)
display(answers27)
answers['27'] = 'Daniel Radcliffe & Rupert Grint'

display(answers)