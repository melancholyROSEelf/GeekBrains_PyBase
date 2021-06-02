# Задача 4
print('Задача 4\n')

from translate import Translator

translator = Translator(from_lang='english', to_lang='russian')

with open('text_task4_1.txt') as text_1:
    with open('text_task4_2.txt', 'w+') as text_2:
        for line in text_1:
            text_2.write(f'{translator.translate(line)}\n')

        text_2.seek(0)
        print(text_2.read())
