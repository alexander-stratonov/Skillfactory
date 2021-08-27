import pandas as pd
from IPython.display import display
#df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
rating_pd = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/ratings.csv')
movies_pd = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/movies.csv')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df)
display(rating_pd)
display(movies_pd)
joined = rating_pd.merge(movies_pd, on='movieId', how='left')
with pd.option_context('display.max_columns', None):
    display(joined) 