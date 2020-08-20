# Любимый вариант очереди Тимофея - очередь, написанная с использованием связного списка. 
# Помогите ему с реализацией. Очередь должна поддерживать методы get, put, size.

# Формат ввода
# В первой строке записано количество команд n - целое число, не превосходящее 1000. 
# В каждой из следующих n строк записана команда: get, put, или size.

# Формат вывода
# При вызове метода get напечатайте возвращаемое значение. 
# Если метод get вызывается у пустой очереди, нужно напечатать 'error'. 
# При вызове метода size - вывести размер очереди.

# Пример 1
# Ввод	
# 10
# put -34
# put -23
# get
# size
# get
# size
# get
# get
# put 80
# size
# Вывод
# -34
# 1
# -23
# 0
# error
# error
# 1

class MyQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return 'error'
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[0]


t = int(input())
stack = MyQueue()
while t:
    l = input().split()
    if l[0] == 'put':
        stack.push(int(l[1]))
    if l[0] == 'get':
        print(stack.pop())
    if l[0] == 'size':
        print(stack.size())
    if l[0] == 'peek':
        print(stack.peek())
    t -= 1
