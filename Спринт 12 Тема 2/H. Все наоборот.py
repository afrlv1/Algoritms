# Вася решил запутать маму —– делать дела в обратном порядке. 
# Список его дел теперь хранится в двусвязном списке. 
# Напишите функцию, которая вернёт список в обратном порядке.
class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev

def solution(node):
    prev = None
    ta = node
    while ta:
        next = ta.next
        ta.next = prev
        prev = ta
        ta = next
        node = prev
    return node
