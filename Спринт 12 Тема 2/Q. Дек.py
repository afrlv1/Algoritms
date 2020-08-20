# Гоша решил реализовать структуру данных Дек, 
# максимальный размер которого определяется заданным числом. 
# Методы push_back, push_front, pop_front, pop_back работали корректно. 
# Но, если в деке было много элементов, программа работала очень долго. 
# Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! 
# Напишите эффективную реализацию.

# Формат ввода
# В первой строке записано количество команд n - целое число, не превосходящее 5000. 
# Во второй строке записано число m - максимальный размер стека. Он не превосходит 1000. 
# В следующих n строках записана одна из команд: 
# push_back value
# push_front value
# pop_front
# pop_back
# value - целое число, по модулю не превосходящее 1000.

# Формат вывода
# При вызове команд pop_front и pop_back нужно вывести возвращаемое значение. 
# Если они вызываются для пустого стека - напечатайте 'error'. 
# Если команда push_back или push_front вызывается для стека, размер которого равен 
# максимально возможному, тоже нужно вывести 'error'.

# Пример 1
# Ввод	
# 4
# 4
# push_front 861
# push_front -819
# pop_back
# pop_back
# Вывод
# 861
# -819

class MyQueue:
    def __init__(self, n):
        self.items = []
        self.max_n = n
        self.siz = 0
    def isEmpty(self):
        return self.items == []
    
    def push_front(self, item):
        if self.siz != self.max_n:
            self.items.insert(0, item)
            self.siz += 1
        else:
            print('error')

    def push_back(self, item):
        if self.siz != self.max_n:
            self.items.append(item)
            self.siz += 1
        else:
            print('error')

    def pop_front(self):
        if self.isEmpty():
            return 'error'
        self.siz -= 1
        return self.items.pop(0)

    def pop_back(self):
        if self.isEmpty():
            return 'error'
        self.siz -= 1
        return self.items.pop()

    def size(self):
        return self.siz


t = int(input())
v = int(input())
stack = MyQueue(v)
while t:
    l = input().split()
    if l[0] == 'push_front':
        stack.push_front(int(l[1]))
    if l[0] == 'push_back':
        stack.push_back(int(l[1]))
    if l[0] == 'pop_front':
        print(stack.pop_front())
    if l[0] == 'pop_back':
        print(stack.pop_back())    
    if l[0] == 'size':
        print(stack.size())
    if l[0] == 'peek':
        print(stack.peek())
    t -= 1