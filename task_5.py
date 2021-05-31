# Задача 5
print('Задача 5\n')

from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def func(el_prev, el):
    """
    Возвращает произведение элементов.

    Позиционные аргументы:
    el_prev: предшествующий элемент
    el: текущий элемент

    """

    return el_prev * el


print(reduce(func, my_list))
