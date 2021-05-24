print('Задача 6\n')
check = 'y'
items = []
item_dict = {
    'Название': '',
    'Цена': '',
    'Количество': '',
    'Единица измерения': ''
}
number = 1
items_records = {
    'Название': [],
    'Цена': [],
    'Количество': [],
    'Единица измерения': []
}

while check == 'y':
    check = input('Хотите добавить товар (y/n)?: ')

    if check == 'y':
        item_dict['Название'] = input('Введите название товара: ')
        item_dict['Цена'] = input('Введите цену товара: ')
        item_dict['Количество'] = input('Введите количество товара: ')
        item_dict['Единица измерения'] = input('Введите единицу измерения товара: ')

        if item_dict['Название'] not in items_records['Название']:
            items_records['Название'].append(item_dict['Название'])

        if item_dict['Цена'] not in items_records['Цена']:
            items_records['Цена'].append(item_dict['Цена'])

        if item_dict['Количество'] not in items_records['Количество']:
            items_records['Количество'].append(item_dict['Количество'])

        if item_dict['Единица измерения'] not in items_records['Единица измерения']:
            items_records['Единица измерения'].append(item_dict['Единица измерения'])

        items.append((int(number), dict(item_dict)))
        number += 1

    elif check == 'n':
        break

print(items)
print(items_records)
