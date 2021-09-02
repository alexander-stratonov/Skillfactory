import pandas as pd
from IPython.display import display
users = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/users.csv')
log = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/log.csv', header = None)
#users = pd.read_csv('C:/Users/user/Downloads/users.csv')
#log = pd.read_csv('C:/Users/user/Downloads/log.csv')
display(users)
with pd.option_context('display.max_columns', None):
    display(log)
