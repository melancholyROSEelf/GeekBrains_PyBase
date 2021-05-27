# Задача 5
print('Задача 5\n')

print('Символ останавливающий программу - $\n')

num_str = ' '
num_sum = 0
num_list = []

while True:
    num_str = input('Введите числа через пробел: ')

    if num_str[0] == '$':
        break

    elif num_str[-1] == '$':
        for el in num_str[:-2]:
            if el == ' ':
                continue

            num_list.append(float(el))

        num_sum += sum(num_list)

        print(num_sum)

        break

    for el in num_str:
        if el == ' ':
            continue

        num_list.append(float(el))

    num_sum += sum(num_list)

    print(num_sum)
    num_list.clear()
