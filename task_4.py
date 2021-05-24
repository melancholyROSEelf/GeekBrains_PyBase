print('Задача 4\n')
letter = input('Введите текст: ')
word = ''
number = 1

if letter[-1] != ' ':
    letter += ' '

for i in letter:
    word += i

    if i == ' ':
        if len(word) > 10:
            print(f'{number}. {word[:10]}')
            word = ''
            number += 1

        else:
            print(f'{number}. {word}')
            word = ''
            number += 1
