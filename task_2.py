# Карачевцева Анастасия 44-22-122 задание 2
import math
import sys
import unittest


def main(*args):
    try:
        x = float(args[0][1])
        if x < 3:
            return x * math.cos(x) ** 2 + x
        else:
            return math.sqrt(x) * math.cos(0.0421) * x ** 2
    except:
        return "Произошла ошибка"

class SolverOfASystemOfEquationsTestCase(unittest.TestCase):
    def test_le(self):
        res = main(['...', 0.5])
        self.assertEqual(res, 0.8850755764670349)

    def test_r(self):
        res = main(['...', 0.9])
        self.assertEqual(res, 1.2477590573881108)

    def test_error(self):
        res = main()
        self.assertEqual(res, "Произошла ошибка")