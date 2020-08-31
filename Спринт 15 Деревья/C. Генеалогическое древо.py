# Гуляя по вилле Кондратия, ребята нашли генеалогическое древо его семьи. 
# Им стало интересно, сколько лет прожили члены семьи разных поколений.
# Помогите ребятам это выяснить.


class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left



def solution(Node):
    res, stack = [], [(Node, 0)]
    while stack:
        curr, level = stack.pop()
        if curr:
            if len(res) < level + 1:
                res.append([])
            res[level].append(curr.value)
            stack.append((curr.right, level+1))
            stack.append((curr.left, level+1))
    return res