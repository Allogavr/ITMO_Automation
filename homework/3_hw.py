def task_1(a, b):
    if a > b:
        print(a)
    else:
        print(b)


task_1(7.8, 5.6)


def task_2(c, d):
    if c - d == 135 or c - d == -135:
        print('yes')
    else:
        print('no')


task_2(-1, -136)


def season(month: int):
    if month in range(1, 3) or month == 12:
        print('Зима')
    elif month in range(3, 6):
        print('Весна')
    elif month in range(6, 9):
        print('Лето')
    elif month in range(9, 12):
        print('Осень')
    else:
        print('Введите номер месяца от 1 до 12')


season(12)


def task_4(x, y, z):
    if x > 10 and y > 10 and z > 10:
        print('yes')
    else:
        print('no')


task_4(11, 12, -30)


listok = [45, -25, 3.3, -3, 0]
pos = 0
for num in listok:
    if num > 0:
        pos += 1
print('Количество положительных числе в списке: ', pos)


def task_6(g: int, m: int):
    return g * 12 * 29 + m * 29


print(task_6(1, 1))
