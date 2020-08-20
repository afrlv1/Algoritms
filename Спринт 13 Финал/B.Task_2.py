# Посылка № 33761477

# Типовой ввод для контеста:
with open('input.txt') as f:
    n = int(f.readline())  # Длина массива
    k = int(f.readline())  # искомый элемент к
    arr = list(map(int, (f.readline().split())))  # положительные числа
# Поиск индекс искомого элемента к в массиве
for i in range(n):
    if arr[i] == k:
        pos = i
        break
    else:
        pos = -1
print(pos)
