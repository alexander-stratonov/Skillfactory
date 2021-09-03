import pandas as pd
from IPython.display import display
users = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/users.csv')
log = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/log.csv', header = None)
#users = pd.read_csv('C:/Users/user/Downloads/users.csv', sep=';', encoding = 'koi8_r')
#users.columns = ['user_id', 'email', 'geo']
#log = pd.read_csv('C:/Users/user/Downloads/log.csv', header = None)
log.columns = ['user_id', 'time', 'bet', 'win']
sample = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/sample.csv')
#sample = pd.read_csv('C:/Users/user/Downloads/sample.csv')
display(sample)

#1
sample2 = sample.copy()
sample2.Age = sample.Age.apply(lambda a : a + 1)
display(sample2)

#2
sample2.City = sample.City.apply(lambda b : str(b).lower())
display(sample2)

#3
sample3 = sample.copy()
def profession_code(c):
    if c == 'Рабочий':
        return 0
    elif c == 'Менеджер':
        return 1
    else:
        return 2
sample3['Profession'] = sample.Profession.apply(profession_code)
display(sample3)