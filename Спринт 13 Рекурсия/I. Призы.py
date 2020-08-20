# В конкурсе на самую быструю программу сортировки одинаковый результат получили k человек. 
# В призовом фонде имеется n монет различного достоинства. Нужно определить, можно ли разделить 
# их между победителями таким образом, чтобы каждый получил одинаковую сумму.

# Формат ввода
# В первой строке задано k - количество победителей - целое число от 1 до 16. 
# Во второй строке задано n - количество монет - целое число, не превосходящее 16. 
# Далее в строку через пробел записано n чисел, каждое из которых не превосходит 10000.

# Формат вывода
# Нужно вывести True, если возможно разделить призовой фонд на равные части между победителями, 
# иначе - False.

# Пример 1
# Ввод	
# 4
# 7
# 4 3 2 3 5 2 1
# Вывод
# True

def get_result(nums, k):
    s = sum(nums)
    if s % k != 0:
        return False
    used = [0] * len(nums)
    return can_split_coins(0, nums, 0, k, used, s // k)


def can_split_coins(start, nums, bucket, k, used, t):
    if k == 1:
        return True 
    if bucket == t:
        return can_split_coins(0, nums, 0, k - 1, used, t)
    for i in range(start, len(nums)):
        if used[i] != 1 and bucket + nums[i] <= t:
            used[i] = 1
            if can_split_coins(i + 1, nums, bucket + nums[i], k, used, t):
                return True

            used[i] = 0
    return False
input_data = []
with open('input.txt') as fp:
    line = fp.readline().strip()
    while line:
        input_data.append(line)
        line = fp.readline().strip()
k, _, data = int(input_data[0]), input_data[1], input_data[2]
arr = list(map(int, (data.split())))
print(get_result(arr, k))