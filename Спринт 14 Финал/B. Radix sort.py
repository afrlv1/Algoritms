"""

Когда Кондратий узнал про алгоритм поразрядной сортировки, он объявил конкурс на самую быструю
реализацию алгоритма. Вы тоже принимаете участи в этом конкурсе. Успехов!
Формат ввода

В первой строке задано n - длина массива неотрицательных целых чисел, каждое из которых не
превосходит 100000.
В следующей строке через пробел записаны n чисел.
Формат вывода

Выведите числа в отсортированном по неубыванию порядке.
Пример 1

Ввод
8
0 45 75 90 802 24 2 66
Вывод
0 2 24 45 66 75 90 802

Пример 2
Ввод	Вывод
5
0 37 1 50 12
Вывод
0 1 12 37 50

Пример 3
Ввод
5
7 36 2 25 6
Вывод
2 6 7 25 36
"""


def radixsort(arr):
    radix = 10
    maxlength = False
    tmp, placement = -1, 1

    while not maxlength:
        maxlength = True
        buckets = [list() for _ in range(radix)]
        for  i in arr:
            tmp = i // placement
            buckets[tmp % radix].append(i)
            if maxlength and tmp > 0:
                maxlength = False

        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        placement *= radix
    return arr


n = int(input())
arr = list(map(int, input().split()))
print(radixsort(arr))

