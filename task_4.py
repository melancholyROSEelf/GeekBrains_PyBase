# Задание 4
print('Задание 4\n')


class Car:
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self):
        Car.speed = int(input('Скорость: '))
        Car.color = input('Цвет: ')
        Car.name = input('Марка: ')
        Car.is_police = bool('True or False: ')

    def go(self):
        print('Ура поехали!')

    def stop(self):
        print('Остановка..')

    def turn(self, direction):
        print(f'Поварачиваем {direction}')

    def show_speed(self):
        print(f'Скорость: {Car.speed}')


class TownCar(Car):
    def show_speed(self):
        if Car.speed > 60:
            print(f'Скорость: {Car.speed}')
            print('Слишком быстро!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if Car.speed > 40:
            print(f'Скорость: {Car.speed}')
            print('Слишком быстро!')


class PoliceCar(Car):
    pass


t = TownCar()
t.go()
t.stop()
t.turn(input('Куда поворачиваем?: '))
t.show_speed()

s = SportCar()
s.go()
s.stop()
s.turn(input('Куда поворачиваем?: '))
s.show_speed()

w = WorkCar()
w.go()
w.stop()
w.turn(input('Куда поворачиваем?: '))
w.show_speed()

p = PoliceCar()
p.go()
p.stop()
p.turn(input('Куда поворачиваем?: '))
p.show_speed()
