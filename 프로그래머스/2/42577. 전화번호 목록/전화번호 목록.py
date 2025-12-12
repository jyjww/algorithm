class Node:
    def __init__(self):
        self.children = {}
        self.end = False
def solution(phone_book):
    root = Node()
    
    for p in phone_book:
        node = root
        for ch in p:
            if node.end:
                return False
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        
        if node.end or node.children:
            return False
        node.end = True
    return True