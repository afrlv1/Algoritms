# Рита захотела подзаработать денег и решила поиграть на бирже. 
# Она подумала, что сначала нужно потренироваться на исторических данных.

# Дан массив цен акций. На i-й позиции массива — цена в i-й день. 
# Акции можно покупать и продавать, но только по одной штуке. 
# В одно время не должно быть более одной открытой транзакции.

# Помогите Рите выяснить, какую максимальную прибыль она может получить.

# Формат ввода
# В первой строке записано целое число n. Оно находится в диапазоне от 0 до 10000.

# Во второй строке через пробел записаны n целых чисел в диапазоне от 0 до 1000.

# Формат вывода
# Нужно вывести число, равное максимально возможной прибыли за эти дни.

# Пример 1
# Ввод	
# 6
# 7 1 5 3 6 4
# Вывод
# 7

ch = input()
s = list(map(int, (input().split())))
summa = 0
mins = s[0]
maxs = 0
s.pop(0)
for x in s:
    if x < maxs:
        summa += maxs - mins
        mins = x
        maxs = 0
    elif x < mins:
        mins = x
    elif x > maxs and x > mins:
        maxs = x
if s[-1] == maxs and maxs > mins:
    summa += maxs - mins
print(summa)