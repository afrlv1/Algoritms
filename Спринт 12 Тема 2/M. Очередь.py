# Перед Тимофеем стоит задача написать несколько реализаций собственной очереди, 
# так как доступные на рынке варианты для проекта не подходят. 
# Требования к первой вот такие: класс должен называться MyQueue(), 
# поддерживать операции добавления, удаления, получения элемента, 
# определение текущего размера, и метод, показывающий, пуста ли очередь или нет. 
# Реализована структура данных должна быть на основе массива.

# Формат ввода
# В первой строке записано одно число - количество команд, оно не превосходит 5000. 
# Далее идут команды по одной в строке. Команды могут быть следующих видов:
# push x - добавить число x в очередь
# pop - удалить число из очереди и напечатать его
# peek - напечатать первое число в очереди
# size - вернуть размер очереди
# Формат вывода
# Для каждой команды size, peek и pop напечатайте результат её выполнения. 
# Если очередь пуста, для команды peek напечатайте None. 
# Если происходит удаление из пустой очереди — напечатайте None.

# Пример 1
# Ввод	
# 10
# size
# push 0
# pop
# push 2
# size
# push -2
# pop
# push -8
# push 4
# push 6
# Вывод
# 0
# 0
# 1
# 2

class MyQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
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
    if l[0] == 'push':
        stack.push(int(l[1]))
    if l[0] == 'pop':
        print(stack.pop())
    if l[0] == 'size':
        print(stack.size())
    if l[0] == 'peek':
        print(stack.peek())
    t -= 1