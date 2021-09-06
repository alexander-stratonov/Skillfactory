a1 = int(input('Введите число: '))
s = a1
s2 = 0+a1**2
while s!=0:
    a1 = int(input())
    s = s+a1
    print('Тeкущая сумма:', s)
    s2 = s2 + a1**2
    if s==0:
        break
print('Сумма квадратов всех введенных чисел:', s2)