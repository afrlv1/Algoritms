# Даны 2 массива, отсортированные по неубыванию, а также число k. 
# Нужно определить пары, которые имеют наименьшую сумму. 
# При этом пара должна состоять из одного элемента первого массива, и 
# одного элемента второго. 
# Нужно найти k таких пар с наименьшей суммой.


# Ввод	
# 3
# 1 7 11
# 3
# 2 4 6
# 3
# Вывод
# 1 2
# 1 4
# 1 6

with open('input.txt') as f:
    n1 = int(f.readline())
    nums1 = list(map(int, (f.readline().split())))
    n2 = int(f.readline())
    nums2 = list(map(int, (f.readline().split())))
    k = int(f.readline())
import heapq

def small(nums1, nums2, k, n1, n2):
    result = []
    
    if n1 == 0 or n2 == 0:
        return result
    heap = [(nums1[i1] + nums2[0], i1, 0) for i1 in range(n1)]
    heapq.heapify(heap)
    while len(result) < k and len(heap) > 0:
        s, i1, i2 = heapq.heappop(heap)
        result.append(sorted((nums1[i1], nums2[i2])))
        i2 += 1
        if i2 < n2:
            heapq.heappush(heap, (nums1[i1] + nums2[i2], i1, i2))
    result.sort()
    for i in result:
        print(*i)
small(nums1, nums2, k, n1, n2)