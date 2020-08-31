# Прабабке Кондратия уже 182 года. Домна Тарасовна часто любит выходить в сад погулять. 
# Сегодня, выходя на прогулку, она забыла очки, без которых почти ничего не видит. 
# Но она может прекрасно ориентироваться при помощи трости. 
# Ей она и определила, что приближается к дереву. 
# Что бы увидела баба Домна, если бы не забыла очки?


class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

import collections
def solution(root):

    if root is None: return []
    nodes = collections.defaultdict(list)
    traverse(root, 0, nodes)

    return [x[0] for x in nodes.values()]

def traverse(root, level, nodes):
    nodes[level].append(root.value)
    if root.left: traverse(root.left, level+1, nodes)
    if root.right: traverse(root.right, level+1, nodes)   