# Рита захотела оптимизировать алгоритм быстрой сортировки. 
# Алгоритму не должно требоваться O(n) дополнительной памяти. А у вас получится?
# Формат ввода
# В первой строке на вход подается число n - длина массива. n не превосходит 1000. 
# Во второй строке через пробел записаны n чисел. Каждое из чисел по модулю не превосходит 1000.
# Формат вывода
# Нужно вывести через пробел числа в отсортированном по возрастанию порядке.

# Пример 1
# Ввод	
# 14
# 5 3 7 2 8 26 -12 -30 -10 27 13 -20 -30 18
# Вывод
# -30 -30 -20 -12 -10 2 3 5 7 8 13 18 26 27
with open('input.txt') as f:
    n = int(f.readline())
    a = list(map(int, (f.readline().split())))
def partition(nums, low, high):  
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]
def quick_sort(nums):  
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

# Проверяем, что оно работает
random_list_of_nums = a 
quick_sort(random_list_of_nums)  
print(*(random_list_of_nums) )