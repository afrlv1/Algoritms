# Гоше стало интересно, можно ли разбить все заработанные им во время игры в 
# Лампу очки на две части так, чтобы сумма в них была одинаковой.

# Формат ввода
# В первой строке записано число элементов массива n. Оно не превосходит 10000

# Далее в строку записаны n целых неотрицательных чисел, каждое из которых не превосходит 10000

# Формат вывода
# Нужно вывести True, если произвести такое разбиение возможно, иначе — False

# Пример 1
# Ввод	
# 4
# 1 5 7 1
# Вывод
# True

def canPartition(nums):
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums)/2
    values = {0, nums[0]}
    i = 1
    while target not in values and i < len(nums):
        values = values.union([v+nums[i] for v in values])
        i += 1
    return target in values
n = input()
arr = list(map(int, (input().split())))
print(canPartition(arr))