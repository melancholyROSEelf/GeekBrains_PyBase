# Задача 2
print('Задача 2\n')

str_line_list = []

with open('text_task2.txt') as text:
    for line in text:
        str_line_list.append(line.count(' ') + 1)

for i, el in enumerate(str_line_list):
    print(f'{i + 1} строка: количество слов - {el}')

print(f'\nСтрок в файле: {len(str_line_list)}')
