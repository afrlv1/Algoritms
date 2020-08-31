def heapify(nums, heap_size, root_index):
     #индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2*root_index)+1
    right_child = (2*root_index)+2

     #Если левый потомок корня - это допустимый индекс, а элемент больше
     #чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
         largest = left_child
     # тоже самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    #если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    """создаем Max heap из списка
    второй аргумент означает остановку алгоритма перед элементом -1, то есть
    перед первым элементом списка
    3-ий аргумент означает повторный проход по списку в обратном направлении,
    уменьшая счетчик i на 1
    """
    for i in range(n, -1, -1):
        heapify(nums,n,i)
    # перемещаем корень Max Heap в самый конец списка
    for i in range (n-1,0,-1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums,i,0)

# проверяем что все работает
random_list_of_nums = [35,12,43,8,51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)