# После чая с печеньками ребята решили поиграть в игру. 
# Дан набор строк одинаковой длины, состоящих из маленьких латинских букв. 
# Нужно определить, какое минимальное число позиций в каждой из строк нужно удалить, 
# чтобы буквы в строках, соответствующие каждому индексу из оставшихся, были лексикографически 
# отсортированы по неубыванию.

# Формат ввода
# В первой строке записано число n - количество строк.
# Во второй - m - длина каждой из строк.
# Оба числа не превосходят 1000.
# В каждой из следующих n строк записана строка, состоящая из m строчных букв латинского алфавита.

# Формат вывода
# Нужно вывести одно число - минимальное количество индексов, которые нужно удалить, 
# чтобы выполнялось указанное требование.

# Пример 1
# Ввод	
# 3
# 3
# cba
# daf
# ghi
# Вывод
# 1

n = int(input())
m = int(input())
li = []
while n:
    li.append(input())
    n -= 1
transposed = zip(*li)
k = 0
for x in transposed:
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            k += 1
            break
print(k)