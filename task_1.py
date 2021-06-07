# Задание 1
print('Задание 1\n')

import time


class TrafficLight:
    __color = None

    def running(self):
        __color = 'red'
        print(__color)
        time.sleep(7)

        __color = 'yellow'
        print(__color)
        time.sleep(2)

        __color = 'green'
        print(__color)
        time.sleep(1)


traf_l = TrafficLight()
traf_l.running()
