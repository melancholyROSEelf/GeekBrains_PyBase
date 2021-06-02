# Задача 1
print('Задача 1\n')

text_in = None

with open('text_task1.txt', 'w+') as text:
    while text_in != '\n':
        text_in = input('Введите что-нибудь: ') + '\n'
        text.write(text_in)

    text.seek(0)
    print(text.read())
