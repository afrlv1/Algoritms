# Вася размышляет, что бы такое из списка не делать. Но, кажется, все пункты очень важные! 
# Вася решает загадать число и удалить дело, которое идёт под этим номером. 
# Список дел представлен в виде односвязного списка. Напишите функцию solution, 
# которая принимает на вход голову списка и номер удаляемого дела и возвращает 
# голову обновлённого списка.
# Узел списка описывается следующим классом:

class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_ite

def solution(node, n):
    head = node
    if n == 0:
        head = node.next_item
        return head
    while n - 1:
        node = node.next_item
        n -= 1
    node.next_item = node.next_item.next_item
    return head