"""Lesson_1"""
# Task_1

var_int = 123
var_float = 1.23
var_str = '123'
var_list = [1, var_float, 'Jerry', [1, '2', 0.3]]

print(var_int, var_float, var_str, var_list)
print()

number_1 = int(input('Введите целое число: '))
number_2 = float(input('Введите дробное число: '))

print(number_1, number_2)
print()

string_1 = input('Введите что-нибудь: ')
string_2 = input('Введите что-нибудь ещё: ')

print(string_1, string_2)
print()

# Task_2

time = int(input('Введите время в секундх: '))
hours = int(time / 60 / 60)
minutes = int(time / 60 % 60)
seconds = int(time % 60)

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

if seconds < 10:
    seconds = '0' + str(seconds)

print(f'Время сейчас: {hours}:{minutes}:{seconds}')
print()

# Task_3

number = input('Введите число: ')
sum_number = int(number) + int(number * 2) + int(number * 3)

print('Сумма равна:', sum_number)
print()

# Task_4

number = input('Введите число: ')
number_list = list(number)
print(number_list)
number_max = 0

while len(number_list) != 0:

    if number_max - int(number_list[0]) < 0:
        number_max = int(number_list[0])

    number_list.pop(0)


print('Наибольшая цифра в числе:', number_max)
print()

# Task_5

proceeds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
profit = proceeds - costs
profitability = str(int(round((profit / proceeds), 2) * 100)) + '%'
workers = int(input('Введите число сотрудников фирмы: '))

if proceeds > costs:
    print('Фирма работает прибыльно!')
    print('Рентабельность выручки:', profitability)
    print('Прибыль фирмы в расчете на одного сотрудника:', profit / workers)
    print()

else:
    print('Фирма работает в убыток :(')
    print('Убыток фирмы в расчете на одного сотрудника:', profit / workers)
    print()

# Task_6

a = int(input('Введите результат спортсмена в первый день: '))
b = int(input('Введите результат, которого спортсмен хочет достичь: '))
day = 1

print('1-й день:', a)

while a < b:
    a = round((a * 1.1), 2)
    day += 1
    print(str(day) + '-й день:', a)

print()
print('На ' + str(day) + '-й день спортсмен достиг результата - не менее ' + str(b) + ' км.')
