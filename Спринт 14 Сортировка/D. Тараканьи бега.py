"""
Сегодня 31 апреля, и в Удотинске по традиции проводятся тараканьи бега. Забеги разделены на две категории.
Если таракан участвовал в забеге одной из категорий, он не может принимать участие в забегах другой
категории. Но встречаются нарушители! Помогите судьям их выявить и восстановить справедливость.

Есть два списка со стартовыми номерами тараканов. Нужно вывести номера, которые встречаются и в первом,
и во втором списке. Квадратичный алгоритм не подойдет для этой задачи. Тараканы разбегутся, пока
алгоритм закончит работу.

Формат ввода
В первой строке записано число n - длина первого списка.
Во второй строке - число m - длина второго списка.
Оба числа не превосходят 10000
В следующих двух строках через пробел могут быть записаны два списка соответствующей длины,
состоящие из чисел, не превосходящих 10000.

Формат вывода
Нужно в строку вывести стартовые номера тараканов в порядке, в котором они встречались в первом списке.

Пример 1
Ввод
3
5
4 9 5
9 4 9 8 4
Вывод
4 9
Пример 2
Ввод
3
8
7 8 10
9 7 5 3 6 6 4 1
Вывод
7
"""
n = int(input())
m = int(input())
arr_1 = list(map(int, input().split())) if n else list()
arr_2 = list(map(int, input().split())) if m else list()
arr_3 = []

for i in range(len(arr_1)):
    if arr_1[i] in arr_2:
        if arr_2[i] not in arr_3:
            arr_3.append(arr_2[i])

print(*arr_3)
