# Карачевцева Анастасия 44-22-122 задание 1
import math
import sys


def main(*args):
    try:
        x = float(args[0][0])
        if x < 3:
            return x * math.cos(x) ** 2 + x
        else:
            return math.sqrt(x) * math.cos(0.0421) * x ** 2
    except:
        return "Произошла ошибка"

print(main(sys.argv[1:]))