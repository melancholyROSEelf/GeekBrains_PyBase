"""Lesson_2"""

check = 'y'
number_task = None

while check == 'y':
    check = input('Хотите выполнить задачу (y/n)?: ')

    if check == 'y':
        number_task = int(input('Напишите номер задачи: '))

        if number_task == 1:
            import task_1

        elif number_task == 2:
            import task_2

        elif number_task == 3:
            import task_3

        elif number_task == 4:
            import task_4

        elif number_task == 5:
            import task_5

        elif number_task == 6:
            import task_6

    elif check == 'n':
        break

print('\nДоброго дня!')
