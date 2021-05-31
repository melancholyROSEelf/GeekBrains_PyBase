# Задача 2
print('Задача 2\n')

old_list = [7, 15, 2, 0, 96, 135, -8, 52]
new_list = [el for el in old_list
            if el > old_list[old_list.index(el) - 1]
            and old_list.index(el) != 0]

print(new_list)
