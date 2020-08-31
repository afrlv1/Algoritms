# Ребята решили поиграть в игру. 
# Дано дерево, в узлах которого записаны цифры от 0 до 9. 
# Таким образом, каждый путь от корня до листа содержит число, 
# получившееся конкатенацией цифр пути. 

class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left



def solution(root):
    def dfs(root):
        if not root:
            return
        if not root.left and not root.right:
            tmp.append(str(root.value))
            res.append("".join(tmp))
            tmp.pop()
            return
        tmp.append(str(root.value))
        dfs(root.left)
        dfs(root.right)
        tmp.pop()
    tmp = []
    res = []
    dfs(root)
    res = sum(list(map(int, res)))
    return res