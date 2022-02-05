"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from random import randint


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    a = max(map(lambda i: (array.count(i), i), set(array)))
    return f'Чаще всего встречается число {a[1]}, ' \
           f'оно появилось в массиве {a[0]} раз(а)'


#array = [1, 1, 3, 1, 3, 4, 5]
array = [randint(1, 6) for i in range(50)]
#print(func_1())
#print(func_2())
#print(func_3())
print('# func_1', timeit('func_1()', globals=globals(), number=100000), 'seconds')
print('# func_2', timeit('func_2()', globals=globals(), number=100000), 'seconds')
print('# func_3', timeit('func_3()', globals=globals(), number=100000), 'seconds')

# на маленьких массивах лучше работает "func_1()" цикл со счетчиком,
# но при увеличении размера массива, лучше начинает работать "func_3()" в паре "set", "max"

'''-- len(array) = 5 --'''
# func_1 0.05703979998361319 seconds
# func_2 0.07692170000518672 seconds
# func_3 0.0851503000012599 seconds

'''-- len(array) = 20 --'''
# func_1 0.2947405000159051 seconds
# func_2 0.3485557000094559 seconds
# func_3 0.166222799976822 seconds

'''-- len(array) = 50 --'''
# func_1 1.4624989000149071 seconds
# func_2 1.593189600011101 seconds
# func_3 0.28915960001177154 seconds
