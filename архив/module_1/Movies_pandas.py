import pandas as pd
from IPython.display import display
ratings = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/ratings.csv')
movies = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/movies.csv')
#ratings = pd.read_csv('C:/Users/user/Downloads/ratings.csv')
#movies = pd.read_csv('C:/Users/user/Downloads/movies.csv')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df)
display(ratings[ratings.rating == 0.5]) 
display(movies[movies.movieId == 3456]) 
joined = ratings.merge(movies, on='movieId', how='outer')
#with pd.option_context('display.max_columns', None):
#    display(joined) 