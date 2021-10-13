import pandas as pd
from IPython.display import display
users = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/users.csv')
log = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/log.csv', header = None)
#users = pd.read_csv('C:/Users/user/Downloads/users.csv', sep=';', encoding = 'koi8_r')
#users.columns = ['user_id', 'email', 'geo']
#log = pd.read_csv('C:/Users/user/Downloads/log.csv', header = None)
log.columns = ['user_id', 'time', 'bet', 'win']
sample = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/module_1/sample.csv')
#sample = pd.read_csv('C:/Users/user/Downloads/sample.csv')
display('0.1.', log)
display('0.2', sample)

#1
sample2 = sample.copy()
sample2.Age = sample.Age.apply(lambda a : a + 1)
display('1', sample2)

#2
sample2.City = sample.City.apply(lambda b : str(b).lower())
display('2', sample2)

#3 and 4
def profession_code(c):
    if c == 'Рабочий':
        return 0
    elif c == 'Менеджер':
        return 1
    else:
        return 2
sample2['Profession'] = sample.Profession.apply(profession_code)
display('3, 4', sample2)

#5
print('ЗАДАНИЕ №5')
def age_category(age):
    if age < 23:
        return 'молодой'
    elif 23 <= age <= 35:
        return 'средний'
    elif age > 35:
        return 'зрелый'

#6
print('ЗАДАНИЕ №6')
sample['Age_category'] = sample.Age.apply(age_category)
display(sample)

#7
print('ЗАДАНИЕ №7')
def userid_change(u):
    if u == '#error':
        return''
    else:
        return u.replace('Запись пользователя № - ', '')
log['user_id'] = log.user_id.apply(userid_change)
display(log)

#8
t = log.time[0]
t = str(t).replace('[', '')
display('0', t)

#9
def time_corr(tt):
    if pd.isna(tt):
        return tt
    else:
        return str(tt)[1:]
log.time = log.time.apply(time_corr)
display('0', log)



































