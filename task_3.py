# Задание 3
print('Задание 3\n')


class Worker:
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self):
        Worker.name = input('Имя: ')
        Worker.surname = input('Фамилия: ')
        Worker.position = input('Должность: ')
        Worker._income = {'wage': int(input('Оклад: ')), 'bonus': int(input('Премия: '))}


class Position(Worker):
    def get_full_name(self):
        print(f'{Worker.surname} {Worker.name}')

    def get_total_income(self):
        print(f'{Worker._income["wage"] + Worker._income["bonus"]}')


p = Position()
p.get_full_name()
p.get_total_income()
