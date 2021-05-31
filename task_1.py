# Задача 1
print('Задача 1\n')

from sys import argv

script_name, production, rate, prize = argv

print((int(production) * int(rate)) + int(prize))
