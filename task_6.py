# Задача 6
print('Задача 6\n')

str_dict = {}
sum_num = 0
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('text_task6.txt', encoding='utf-8') as text:
    for line in text:
        str_list = line.split(':')
        subject = str_list[0]

        str_list = [el for el in str_list[1]
                    if el in check_list or el == ' ']

        str_list = ''.join(str_list)[1:].split(' ')

        for el in str_list:
            try:
                sum_num += int(el)

            except ValueError:
                pass

        str_dict.update({subject: sum_num})
        sum_num = 0

print(str_dict)
