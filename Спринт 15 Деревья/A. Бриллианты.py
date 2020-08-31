# У Евлампии есть брошь с бриллиантами в виде дерева. 
# В каждом узле дерева есть какое-то количество бриллиантов. 
# Помогите выяснить, какое максимальное количество бриллиантов есть в одном узле.
# В Трешландии может быть и отрицательное число драгоценных камней в украшении. 




class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution(Node):
    if (Node == None):  
        return float('-inf') 
    res = Node.value 
    lres = solution(Node.left)  
    rres = solution(Node.right)  
    if (lres > res): 
        res = lres  
    if (rres > res):  
        res = rres  
    return res 

