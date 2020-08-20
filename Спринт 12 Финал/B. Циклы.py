# В качестве второго задания финального проекта нужно написать программу, которая определяет, 
# есть ли цикл в связном списке.
# На вход функция принимает голову списка, на выходе должна выдать True, 
# если в списке содержится цикл, иначе — False. 
# Размер дополнительной памяти, к которой обращается функция, не должен превышать О(1).


class Node:  
    def __init__(self, value, next=None):  
        self.value = value  
        self.next = next  
    def __repr__(self):  
        return self.value

def hasCycle(node):
    cur_node = node
    node_list = []
    while cur_node.next is not None:
        prev_node = cur_node
        cur_node = cur_node.next
        if cur_node not in node_list:
            node_list.append(cur_node)
        else:
            prev_node.next = None
            return True
    return False