#  Посылка № 33761465
# Типовой ввод для контеста:
with open('input.txt') as f:
    n = int(f.readline())  # ввод количества фотоцентров
    capacity = list(map(int, (f.readline().split())))  # вместимость фотоцентров


# Расчет максимального количества хранимых фотографий
def photo_bank(capacity, n):
    if n < 2:
        return 0
    capacity.sort()
    photo_hold = 0
    while len(capacity) != 1:
        if not capacity[0]:
            del capacity[0]
        else:
            capacity[0] -= 1
            capacity[-1] -= 1
            photo_hold += 1
            if not capacity[0]:
                del capacity[0]
        capacity.sort()
    return photo_hold


print(photo_bank(capacity, n))
