# Васе нужно распечатать свой список дел на сегодня. Помогите ему: напишите функцию, 
# которая печатает все его дела. Известно, что дел у Васи не больше 
# 5000.
# Формат ввода
# В качестве ответа сдайте только код функции, которая печатает элементы списка.
# Узел списка описывается следующим классом:

class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

def solution(node):
    print(node.value)
    while node.next_item:
        node = node.next_item
        print(node.value)