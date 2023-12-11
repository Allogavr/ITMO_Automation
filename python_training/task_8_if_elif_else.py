num = 4

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


def da_net(str_1, str_2):
    if str_1 in str_2:
        print('Да')
    else:
        print('Нет')


da_net(str_1='test', str_2='testiing')


num_float = 0

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


def zvan(year_of_study: int):
    if year_of_study in range(1, 5):
        print('бакалавр')
    elif year_of_study in range(5, 7):
        print('магистр')
    elif year_of_study in range(7, 10):
        print('аспирант')
    else:
        print('Введите корректный год обучения')


zvan(6)


def chislo(a: int):
    if a > 100 or a < -100:
        print('-')
    else:
        print('+')


chislo(101)
