#Использую код с учебной страницы
import numpy as np
number = np.random.randint(1,101)

#Использую код с учебной страницы
def score_game(game_core):
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


#В алгоритме каждый раз делим оставшийся интервал на 2
def game_core_v2(number):
    number_min = 0
    number_max = 100
    count = 0
    while True:
        predict = round((number_min + number_max)/2)
        count += 1
        if number == predict:
            break
        elif number > predict:
            number_min = predict
        elif number < predict:
            number_max = predict
    return(count)

#Проверяем результат, обычно это 5 попыток
score_game(game_core_v2)