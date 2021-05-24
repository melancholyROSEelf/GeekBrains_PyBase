print('Задача 5\n')
score = [9, 4, 2, 2, 1]
value = None
check = 'y'

while check == 'y':
    check = input('Хотите добавить в рейтинг значение (y/n)?: ')

    if check == 'y':
        value = int(input('Введите значение: '))

        for i in range(len(score)):
            if value > score[i]:
                score.insert(i, value)
                break

            elif value == score[i]:
                if i == (len(score) - 1):
                    score.append(value)
                    break

                elif value != score[i + 1]:
                    score.insert(i + 1, value)
                    break

            elif value < score[i] and i == (len(score) - 1):
                score.append(value)

    elif check == 'n':
        break

print(score)
