# Задача 3
print('Задача 3\n')


def my_func(num_1, num_2, num_3):
    """
    Возвращает сумму двух больших аргументов.

    Позиционные аргументы:
    num_1 -- число
    num_2 -- число
    num_3 -- число

    """
    num_sum = [num_1, num_2, num_3]
    sum_list = [max(num_sum)]

    num_sum.remove(max(num_sum))
    sum_list.append(max(num_sum))

    return sum(sum_list)


print(my_func(int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))))
