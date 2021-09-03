import pandas as pd
from IPython.display import display
#users = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/users.csv')
#log = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/log.csv', header = None)
users = pd.read_csv('C:/Users/user/Downloads/users.csv', sep=';', encoding = 'koi8_r')
#users.columns = ['user_id', 'email', 'geo']
log = pd.read_csv('C:/Users/user/Downloads/log.csv', header = None)
log.columns = ['user_id', 'time', 'bet', 'win']

#1
sample = pd.read_csv('C:/Users/user/Downloads/sample.csv')
sample2 = sample[(sample.Age.apply(lambda x : x + 1))]
display(sample2)
