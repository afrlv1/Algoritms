# Задание связано с обратной польской нотацией. Она используется для парсинга 
# арифметических выражений. По сравнению с другим приемом, применяемым для данной 
# задачи — использованием дерева операций, она является более компактной, 
# так как в ней не используются скобки. Еще её иногда называют обратной польской 
# записью или постфиксной нотацией.

# В постфиксной нотации операнды расположены перед знаками операций.

# Пример 1: 
# 3 4 + 
# будет равно 7, и означает 3 + 4 

# Пример 2: 
# 10 2 4 * - 
# будет равно 2, и означает 10 - 2 * 4 
# Пример 1
# Ввод	
# 2 1 + 3 *
# Вывод
# 9
# Пример 2
# Ввод	
# 7 2 + 4 * 2 +
# Вывод
# 38

class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def plus(self):
        a = self.pop()
        b = self.pop()
        return self.push(a + b)

    def minus(self):
        a = self.pop()
        b = self.pop()
        return self.push(b - a)

    def multi(self):
        a = self.pop()
        b = self.pop()
        return self.push(a * b)

    def division(self):
        a = self.pop()
        b = self.pop()
        return self.push(b // a)

     
s = input().split()
calc = Stack()
for x in s:
    if x == '+':
        calc.plus()
    elif x == '-':
        calc.minus()
    elif x == '*':
        calc.multi()
    elif x == '/':
        calc.division()
    else:
        calc.push(int(x))
print(*(calc.items))
