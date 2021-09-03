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
#1
sample = pd.read_csv('C:/Users/user/Downloads/sample.csv')
display(sample)
sample2 = sample[sample.Age < 30]
display(sample2)
#2
log_win = log[log.win > 0]
display(log_win)
win_count = len(log_win)
display(win_count)
#3
sample2 = sample[(sample.Age < 30) & (sample.Profession == 'Рабочий')]
display(sample2)
#4
log2 = log.query('bet < 2000 & win > 0')
display(log2)
#5
sample3 = sample[sample.City.str.contains ("о", na=False)]
display(sample3)
sample4 = sample[~sample.City.str.contains ("о", na=False)]
display(sample4)
new_log = log[~log.user_id.str.contains ("error", na=False)]
display(new_log)
