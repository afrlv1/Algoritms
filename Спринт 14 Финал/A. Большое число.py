"""
Вечером ребята решили поиграть в игру "Большое число".
Даны числа. Нужно определить, какое самое большое число можно из них составить.
Формат ввода

В первой строке записано n - количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.
Формат вывода

Нужно вывести самое большое число, которое можно из них составить.
Пример 1
Ввод
3
15 56 2
Вывод
56215

Пример 2
Ввод
3
1 783 2
Вывод
78321

Пример 3
Ввод
5
2 4 5 2 10
Вывод
542210
Ввод
6
Ввод
9 6 101 1 1 1
Вывод
96111101
"""

def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba) > int(ab)) - (int(ba) < int(ab)))


def myCompare(mycmp):
    # Конвертировать функцию cmp = в функцию key =
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

if __name__ == "__main__":
    n = int(input())
    a = input().split()
    sorted_array = sorted(a, key=myCompare(comparator))
    number = "".join([str(i) for i in sorted_array])
    print(number)