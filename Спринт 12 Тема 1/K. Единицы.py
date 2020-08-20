# Дано целое положительное число. Нужно посчитать, сколько 1 встречается в 
# двоичной записи этого числа.

# Формат ввода
# На вход подается число в диапазоне от 1 до 10000

# Формат вывода
# Выведите одно число - количество единиц.

# Пример 1
# Ввод	
# 5
# Вывод
# 2
# Пример 2
# Ввод	
# 12
# Вывод
# 2

n = int(input())

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b.count("1"))