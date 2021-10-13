import pandas as pd
from IPython.display import display
users = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/users.csv')
log = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/log.csv', header = None)
#users = pd.read_csv('C:/Users/user/Downloads/users.csv', sep=';', encoding = 'koi8_r')
#users.columns = ['user_id', 'email', 'geo']
#log = pd.read_csv('C:/Users/user/Downloads/log.csv', header = None)
log.columns = ['user_id', 'time', 'bet', 'win']
display('0.1', users)
with pd.option_context('display.max_columns', None):
    display('0.2', log)
#1
sample = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/sample.csv')
#sample = pd.read_csv('C:/Users/user/Downloads/sample.csv')
display('1.1', sample)
sample2 = sample[sample.Age < 30]
display('1.2', sample2)
#2
log_win = log[log.win > 0]
display('2.1', log_win)
win_count = len(log_win)
display('2.2', win_count)
#3
sample2 = sample[(sample.Age < 30) & (sample.Profession == 'Рабочий')]
display('3', sample2)
#4
log2 = log.query('bet < 2000 & win > 0')
display('4', log2)
#5
sample3 = sample[sample.City.str.contains ("о", na=False)]
display('5.1', sample3)
sample4 = sample[~sample.City.str.contains ("о", na=False)]
display('5.2', sample4)
new_log = log[~log.user_id.str.contains ("error", na=False)]
display('5.3', new_log)
