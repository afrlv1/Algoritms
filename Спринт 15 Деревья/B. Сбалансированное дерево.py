# Гоше очень понравилось слушать рассказ Тимофея про деревья. 
# Особенно часть про сбалансированные деревья. 
# Он решил написать функцию, которая определяет, сбалансировано ли дерево.
# Дерево считается сбалансированным, если левое и правое поддеревья 
# каждого узла отличаются по высоте не больше, чем на один.


class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def solution(Node):
    def dfs(Node):
        if not Node:
            return 0, 1
        l, res_l = dfs(Node.left)
        r, res_r = dfs(Node.right)
        if res_l and res_r and (-1 <= l-r <= 1):
            res = 1
        else:
            res = 0
        return max(l,r)+1, res
    return dfs(Node)[1] == 1