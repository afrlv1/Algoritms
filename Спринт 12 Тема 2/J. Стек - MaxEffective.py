# Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума 
# среди элементов в стеке. Сложность операции должна быть O(1). 
# Для пустого стека операция должна возвращать None. 
# При этом push и pop также должны выполняться за константное время.

# Формат ввода
# В первой строке записано одно число - количество команд, оно не превосходит 100000. 
# Далее идут команды по одной в строке. Команды могут быть следующих видов:

# push x - добавить число x в стек
# pop - удалить число с вершины стека
# get_max - напечатать максимальное число в стеке
# Если стек пуст при вызове команды get_max нужно напечатать None, для команды pop - error.
# Формат вывода
# Для каждой команды get_max напечатайте результат её выполнения. 
# Если стек пустой, для команды get_max напечатайте None. 
# Если происходит удаление из пустого стека - напечатайте error.

# Пример 1
# Ввод	
# 10
# pop
# pop
# push 4
# push -5
# push 7
# pop
# pop
# get_max
# pop
# get_max
# Вывод
# error
# error
# 4
# None
# Пример 2
# Ввод	
# 10
# get_max
# push -6
# pop
# pop
# get_max
# push 2
# get_max
# pop
# push -2
# push -6
# Вывод
# None
# error
# None


class StackMax:
    items = []
    maxim = []
    def isEmpty(self):
        return self.items == []
    def get_max(self):
        if self.isEmpty():
            print('None')
            return
        print (self.maxim[-1])
        return
    def push(self, item):
        if self.items:
            last_known_max = self.maxim[-1]
            if item > last_known_max:
                last_known_max = item
            self.items.append(item)
            self.maxim.append(last_known_max)

        else:
            self.items.append(item)
            self.maxim.append(item)
    def pop(self):
        if self.isEmpty():
            print('error')
            return
        result = self.items[-1]
        del self.items[-1]
        del self.maxim[-1]
        return result

t = int(input())
stack = StackMax()
while t:
    l = input().split()
    if l[0] == 'push':
        stack.push(int(l[1]))
    if l[0] == 'pop':
        stack.pop()
    if l[0] == 'get_max':
        stack.get_max()
    t -= 1