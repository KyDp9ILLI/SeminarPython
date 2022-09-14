# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import random
import time


def GetRand(x, y):
    count = y - x
    result = int(time.time()) % count
    return result + x


print(GetRand(13, 222))
# print(time.time())