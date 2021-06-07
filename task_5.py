# Задание 5
print('Задание 5\n')


class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Надеюсь я не забыл дома корректор..')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш так классно скрипит~~~')


class Handle(Stationery):
    def draw(self):
        print('Пахнет не очень.. Т_Т')


p = Pen()
p.draw()

pl = Pencil()
pl.draw()

h = Handle()
h.draw()
