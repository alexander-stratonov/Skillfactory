import pandas as pd
from IPython.display import display
#users = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/users.csv')
#log = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/log.csv', header = None)
users = pd.read_csv('C:/Users/user/Downloads/users.csv', sep=';', encoding = 'koi8_r')
#users.columns = ['user_id', 'email', 'geo']
log = pd.read_csv('C:/Users/user/Downloads/log.csv', header = None)
log.columns = ['user_id', 'time', 'bet', 'win']
display(users)
with pd.option_context('display.max_columns', None):
    display(log)

sample = pd.read_csv('C:/Users/user/Downloads/sample.csv')
display(sample)
columns = sample.columns = ['name', 'city', 'age', 'profession']
display(sample.info())