"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit
from random import sample


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if not el % 2]


def func_3(nums):
    return [i for i in range(len(nums)) if not nums[i] % 2]


nums = [i for i in sample(range(0, 1000000), 1000)]
# print(nums)
#print(func_1(nums))
#print(func_2(nums))
#print(func_3(nums))

print('# func_1', timeit('func_1(nums)', globals=globals(), number=10000), 'seconds')
print('# func_2', timeit('func_2(nums)', globals=globals(), number=10000), 'seconds')
print('# func_3', timeit('func_3(nums)', globals=globals(), number=10000), 'seconds')

'''--Первый замер--'''
# func_1 0.48677869999664836 seconds
# func_2 0.37587320001330227 seconds
# func_3 0.36701909999828786 seconds

'''--Второй замер--'''
# func_1 0.5067141000181437 seconds
# func_2 0.3749934999796096 seconds
# func_3 0.36845750000793487 seconds

'''--Третий замер--'''
# func_1 0.4800460999831557 seconds
# func_2 0.3673922000161838 seconds
# func_3 0.35264420000021346 seconds
