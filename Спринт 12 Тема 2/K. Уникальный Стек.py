# Реализуйте класс StackSet, который хранит только уникальные элементы. 
# При этом операция добавления элемента в стек должна выполняться за O(1).

# Формат ввода
# В первой строке записано одно число - количество команд. Далее идут команды по одной на строке. Команды могут быть следующих видов:

# push x - добавить число x в стек
# pop - удалить число с вершины стека
# peek - напечатать число с вершины стека (без удаления)
# size - узнать размер стека
# Если стек пуст при вызове команд pop и peak нужно вывести на печать error.

# Формат вывода
# Для каждой команды size напечатайте результат её выполнения. 
# Если происходит удаление из пустого стека - напечатайте error.

# Пример 1
# Ввод	
# 8
# push 1
# push 2
# size
# push 2
# size
# pop
# push 1
# size
# Вывод
# 2
# 2
# 1
# Пример 2
# Ввод	
# 10
# push 1
# pop
# push 2
# size
# push 1
# push 2
# pop
# push 2
# peek
# pop
# Вывод
# 1
# 2

class MaxEffective:
    def __init__(self):
        self.items = []
        self.setitems = set()
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        if item not in self.setitems:
            self.items.append(item)
            self.setitems.add(item)
    def pop(self):
        if self.isEmpty():
            print('error')
            return
        else:
            return self.setitems.discard(self.items.pop())
    def peek(self):
        if self.isEmpty():
            return 'error'
        else:
            return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

t = int(input())
stack = MaxEffective()
while t:
    l = input().split()
    if l[0] == 'push':
        stack.push(int(l[1]))
    if l[0] == 'pop':
        stack.pop()
    if l[0] == 'peek':
        print(stack.peek())
    if l[0] == 'size':
        print(stack.size())
    t -= 1