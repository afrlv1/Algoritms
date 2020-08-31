# Гоша понял, что такое дерево поиска, и захотел написать функцию, 
# которая определяет, является ли заданное дерево деревом поиска. 
# Значения в левом поддереве должны быть строго меньше, в правом - строго больше 
# значения в узле.
# Помогите Гоше с реализацией. 

class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution(root):
    pre, cur, stack = None, root, []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        s = stack.pop()
        if pre and s.value <= pre.value:
            return False
        pre, cur = s, s.right
    return True
