# Кондратий приказал найти в его лесу дерево - анаграмму. 
# Гоша и Алла отправились на поиски. Помогите ребятам определить, является ли дерево, 
# которое они нашли деревом - анаграммой?
# Дерево является анаграммой, если оно симметричное относительно своего центра.

class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left



def solution(root):
    def anagramm(L,R):
        if L and R and L.value == R.value: 
            return anagramm(L.left, R.right) and anagramm(L.right, R.left)
        return L == R
    return not root or anagramm(root.left, root.right) 