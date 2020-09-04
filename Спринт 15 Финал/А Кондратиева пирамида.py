# В Трешландии проводились ежегодные соревнования по заезду на барсучьих упряжках.
# Нужно обработать результаты забегов. Данные представлены в формате:
# имя участника - список заработанных очков
# Нужно отсортировать данные по такому принципу:
# Если сумма набранных очков участника A больше, чем у участника В, то А
# должен идти в списке раньше. При подсчете суммы нужно учитывать только
# положительные значения очков.
# Если суммы равны, то первым должен идти участник, чье имя лексикографически меньше.
# При совпадении имен раньше должен идти участник, который во входных данных находится позже.
# При этом, если из имени участника можно составить английский вариант имени Кондратий
# (например, если имя nekondratiy или drkonxxxiyatt), то все правила отменяются.
# Он должен идти в списке раньше. Если таких участников больше одного,
# то раньше должен идти тот, кто находится позже во входных данных.
# (Заработанные очки не рассматриваются).

# Формат ввода
# В первой строке задано n - число участников. Оно не превосходит 10000.
# В следующих n строках записана информация о каждом из участников в обозначенном формате.
# Имя состоит из строчных латинских букв. Длина имени не превосходит 100.
# Длина списка набранных очков не больше 1000. Каждое из очков по модулю не превосходит 1000.

# Формат вывода
# Нужно вывести данные в отсортированном порядке в таком же формате.

# Пример 1
# Ввод
# 3
# anna 1 -4 5 0 1
# sam 1 9 5 0 1
# kondratiy 1 9 5 0 -1
# Вывод
# kondratiy 1 9 5 0 -1
# sam 1 9 5 0 1
# anna 1 -4 5 0 1
# номер посылки 33998378
from collections import namedtuple
Record = namedtuple('Record', 'place name rate sequence')


def _sort_lt_(self, other):
    if self.rate != other.rate:
        return self.rate < other.rate
    elif self.name != other.name:
        return self.name > other.name
    else:
        return self.place < other.place


setattr(Record, '__lt__', _sort_lt_)


def is_name(name):
    return set('kondratiy').issubset(name)


def heapify(arr, arr_length, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < arr_length and arr[index] < arr[left]:
        largest = left
    if right < arr_length and arr[largest] < arr[right]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, arr_length, largest)


def pyramid_sort(arr):
    length = len(arr)
    for index in range(length // 2 - 1, -1, -1):
        heapify(arr, length, index)
    for index in range(length - 1, 0, -1):
        arr[index], arr[0] = arr[0], arr[index]
        heapify(arr, index, 0)


if __name__ == '__main__':
    with open('input.txt') as fd:
        buff = fd.read().splitlines()
        n = int(buff[0])
        top = []
        table = []
        for place, number in enumerate(range(1, n + 1)):
            record = buff[number].split()
            name = record[0]
            sequence = record[1:]
            rate = sum(int(x) for x in sequence if int(x) >= 0)
            if is_name(name):
                top.append(Record(place, name, rate, sequence))
            else:
                table.append((Record(place, name, rate, sequence)))
    if top:
        for item in top[::-1]:
            print(item.name, *item.sequence)
    pyramid_sort(table)
    for item in table[::-1]:
        print(item.name, *item.sequence)