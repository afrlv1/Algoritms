# Евлампии на день рождения подарили два дерева. 
# Кондратий сказал, что они совершенно одинаковые. 
# Но, по мнению Евлампии, они отличаются. 
# Помогите разрешить семейный спор!


class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left
        

def solution(root1, root2): 
    if root1 is None and root2 is None: 
        return True 
    if root1 is not None and root2 is not None: 
        return ((root1.value == root2.value) and 
                solution(root1.left, root2.left)and
                solution(root1.right, root2.right)) 
    return False