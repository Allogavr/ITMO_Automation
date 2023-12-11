def task_1() -> str:
    i: int = 42
    f: float = 47.5
    s: str = 'ITMO'
    l: list = [11, 13, 17]
    b: bool = 27 < 26
    print(i, 'относится к типу', type(i))
    print(f, 'относится к типу', type(f))
    print(s, 'относится к типу', type(s))
    print(l, 'относится к типу', type(l))
    print(b, 'относится к типу', type(b))


task_1()


def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
# Числа Фибоначчи


task_2()


def task_3(a: int) -> int:
    return a ** 2


print(task_3(5))
