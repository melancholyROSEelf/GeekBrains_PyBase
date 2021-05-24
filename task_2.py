print('Задача 2\n')
check = 'y'
value_list = []
itera = None
index = 0

while check == 'y':
    check = input('Хотите добавить в список значение (y/n)?: ')

    if check == 'y':
        value_list.append(input('Введите значение: '))

    elif check == 'n':
        break

itera = int(len(value_list) / 2)

for i in range(itera):
    value_list[index], value_list[index + 1] = value_list[index + 1], value_list[index]
    index += 2

print(value_list)
