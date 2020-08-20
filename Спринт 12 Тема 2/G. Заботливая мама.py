# Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите 
# функцию solution, определяющую индекс первого вхождения передаваемого ей на вход 
# значения в связном списке, если значение присутствует.

class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

def solution(node, elem):
    n = -1
    if node.value == elem:
        return 0
    while node.next_item:
        n += 1
        if node.value == elem:
            return n
        node = node.next_item
    return -1