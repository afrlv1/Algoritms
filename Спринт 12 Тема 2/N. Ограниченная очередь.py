# Далее Тимофею нужно написать класс MyQueueSized(), который принимает параметр max_size, 
# означающий максимально допустимое количество элементов в очереди.

# Формат ввода
# В первой строке записано одно число - количество команд, оно не превосходит 5000. 
# Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000. 
# Далее идут команды по одной на строке. Команды могут быть следующих видов:

# push x - добавить число x в очередь
# pop - удалить число из очереди и вывести на печать
# peek - напечатать первое число в очереди
# size - вернуть размер очереди
# При превышении допустимого размера очереди нужно вывести "error". 
# При вызове операции pop для пустой очереди нужно вернуть None.
# Формат вывода
# Напечатайте результаты выполнения нужных команд, по одному на строке.

# Пример 1
# Ввод	
# 8
# 2
# peek
# push 5
# push 2
# peek
# size
# size
# push 1
# size
# Вывод
# None
# 5
# 2
# 2
# error
# 2

class MyQueue:
    def __init__(self, n):
        self.items = []
        self.max_n = n
        self.siz = 0

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        if self.siz != self.max_n:
            self.items.append(item)
            self.siz += 1
        else:
            print('error')

    def pop(self):
        if self.isEmpty():
            return None
        self.siz -= 1
        return self.items.pop(0)

    def size(self):
        return self.siz

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[0]


t = int(input())
v = int(input())
stack = MyQueue(v)
while t:
    l = input().split()
    if l[0] == 'push':
        stack.push(int(l[1]))
    if l[0] == 'pop':
        print(stack.pop())
    if l[0] == 'size':
        print(stack.size())
    if l[0] == 'peek':
        print(stack.peek())
    t -= 1