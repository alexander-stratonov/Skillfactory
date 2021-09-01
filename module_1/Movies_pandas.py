import pandas as pd
from IPython.display import display
ratings = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/ratings.csv')
movies = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/movies.csv')
#ratings = pd.read_csv('C:/Users/user/Downloads/ratings.csv')
#movies = pd.read_csv('C:/Users/user/Downloads/movies.csv')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df)
joined = ratings.merge(movies, on='movieId', how='left')
with pd.option_context('display.max_columns', None):
    display(joined) 

ratings1 = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/ratings_example.txt', sep = '\t')
movies1 = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/movies_example.txt', sep = '\t')
movies1.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)
display(movies1)
display(ratings1)
display(ratings1.merge(movies1, on = 'movieId', how = 'inner'))
