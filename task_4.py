# Задача 4
print('Задача 4\n')

old_list = [1, 1, 5, 9, 6, 3, 2, 6, 9]
new_list = [el for el in old_list
            if el not in old_list[(old_list.index(el) + 1):]]

print(new_list)
