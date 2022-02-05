"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from timeit import timeit
from memoize import memoize


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


@memoize
def revers_4(enter_num, n=0, count=0, check=False):
    if enter_num == 0:
        if check:
            return '0' * count + str(n)
        else:
            return n
    n = n * 10 + enter_num % 10
    if n == 0:
        count += 1
        check = True
    return revers_4(enter_num // 10, n, count, check)


def revers_5(enter_num):
    revers= ''.join(reversed(str(enter_num)))
    return revers


enter_num = 278227774586863456000
# print(revers(enter_num))
# print(revers_2(enter_num))
# print(revers_3(enter_num))
# print(revers_4(enter_num))
# print(revers_5(enter_num))

print('# revers_1', timeit('revers(enter_num)', globals=globals(), number=100000), 'seconds')
print('# revers_2', timeit('revers_2(enter_num)', globals=globals(), number=100000), 'seconds')
print('# revers_3', timeit('revers_3(enter_num)', globals=globals(), number=100000), 'seconds')
print('# revers_4', timeit('revers_4(enter_num)', globals=globals(), number=100000), 'seconds')
print('# revers_5', timeit('revers_5(enter_num)', globals=globals(), number=100000), 'seconds')

# revers_1 0.28385459998389706 seconds
# revers_2 0.16961909999372438 seconds
# revers_3 0.02052289998391643 seconds
# revers_4 0.011005700012901798 seconds
# revers_5 0.04993330000434071 seconds

# функции "revers", "revers_2" неправильно работают!
# самая эффективная "revers_4" рекурсия с мемори
