# Задача 5
print('Задача 5\n')

sum_num = 0

with open('text_task5.txt', 'w+') as text:
    for el in range(10):
        text.write(f'{el} ')

    text.seek(0)
    num_list = text.read().split(' ')

for i in num_list[:-1]:
    sum_num += int(i)

print(sum_num)
