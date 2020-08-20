# посылка № 33765426

def radixsort(arr):
    radix = 10
    maxlength = False
    tmp, placement = -1, 1

    while not maxlength:
        maxlength = True
        buckets = [list() for _ in range(radix)]
        for i in arr:
            tmp = i // placement
            buckets[tmp % radix].append(i)
            if maxlength and tmp > 0:
                maxlength = False

        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        placement *= radix
    return arr


n = int(input())
arr = list(map(int, input().split()))
print(radixsort(arr))

