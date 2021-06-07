# Задание 2
print('Задание 2\n')


class Road:
    _length = None
    _width = None

    def road_mass(self):
        _length = int(input('Длина полотна (м): '))
        _width = int(input('Ширина полотна (м): '))
        mass_on_depth = int(input('Масса асфальта для покрытия 1 кв.м (кг): '))
        depth = int(input('Ширина полотна (см): '))
        mass_road = int((_length * _width * mass_on_depth * depth) / 1000)

        print(f'{_length} * {_width} * {mass_on_depth} * {depth} = {mass_road} т')


road = Road()
road.road_mass()
