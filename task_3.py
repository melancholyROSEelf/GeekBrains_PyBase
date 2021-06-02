# Задача 3
print('Задача 3\n')

salary = []
salary_sum = []
number = 1

with open('text_task3.txt', encoding='utf-8') as text:
    for line in text:
        str_line_list = line.split(' ')
        salary.append({str_line_list[0][:-1]: float(str_line_list[3])})

print('Список сотрудников, чей оклад меньше 20 тыс.:')
for i in salary:
    for key in i:
        if i[key] < 20:
            print(f'{number}. {key}')
            number += 1

        salary_sum.append(i[key])

print(f'\nСредняя величина дохода сотрудников: {sum(salary_sum) / len(salary_sum)} тыс.')
