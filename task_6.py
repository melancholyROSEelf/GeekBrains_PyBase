# Задача 6
print('Задача 6\n')

from itertools import count, cycle

my_list = list(range(0, 11, 3))
itera = 0

for el in count(-2):
    if el > 1:
        print()
        break

    else:
        print(el)

for el in cycle(my_list):
    if itera > 5:
        break

    else:
        print(el)
        itera += 1
