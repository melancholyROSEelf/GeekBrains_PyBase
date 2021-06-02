# Задача 7
print('Задача 7\n')

import json

firm_list = [{}, {}]
good_firms = 0
bad_firms = 0
profit_firms = 0

with open('text_task7_1.txt') as text_1:
    for line in text_1:
        str_line = line.split(' ')
        firm_name = str_line[0]
        firm_profit = int(str_line[2]) - int(str_line[3])

        if firm_profit > 0:
            print(f'{firm_name}: прибыль - {firm_profit}')

            good_firms += 1
            profit_firms += firm_profit

            firm_list[0].update({firm_name: firm_profit})

        else:
            print(f'{firm_name}: убыток - {abs(firm_profit)}')

            bad_firms += 1

            firm_list[1].update({firm_name: firm_profit})

    print(f'\nСредняя прибыль: {profit_firms / good_firms}\n')

    firm_list.append({'average_profit': profit_firms / good_firms})

    print(firm_list)

    with open('text_task7_2.json', 'w') as text_2:
        json.dump(firm_list, text_2)
