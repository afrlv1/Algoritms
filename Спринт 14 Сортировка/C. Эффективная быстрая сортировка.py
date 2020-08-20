"""
Рита захотела оптимизировать алгоритм быстрой сортировки. Алгоритму не должно требоваться O(n)
дополнительной памяти. А у вас получится?

Формат ввода
В первой строке на вход подается число n - длина массива. n не превосходит 1000.
Во второй строке через пробел записаны n чисел. Каждое из чисел по модулю не превосходит 1000.

Формат вывода
Нужно вывести через пробел числа в отсортированном по возрастанию порядке.

Пример 1
Ввод
14
5 3 7 2 8 26 -12 -30 -10 27 13 -20 -30 18
Вывод
-30 -30 -20 -12 -10 2 3 5 7 8 13 18 26 27
Пример 2
Ввод	Вывод
15
5 3 7 2 8 5 20 -19 -17 22 19 -16 6 11 -1
Вывод
-19 -17 -16 -1 2 3 5 5 6 7 8 11 19 20 22
"""


def quick_sort(arr, start, end):
    if end - start > 1:
        p = partition(arr, start, end)
        quick_sort(arr, start, p)
        quick_sort(arr, p + 1, end)


def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while i <= j and arr[j] >= pivot:
            j = j - 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[start], arr[j] = arr[j], arr[start]
            return j


n = int(input())
arr = list(map(int, input().split())) if n else list()
quick_sort(arr, 0, len(arr))
print(*arr)
