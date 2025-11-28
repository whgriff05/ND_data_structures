class Node:
    def __init__(self, key=None):
        self.key = key
        self.children = {}

    def has_children(self):
        return False if len(self.children.items()) == 0 else True
    
    def get_child(self, key):
        if key not in self.children:
            return None
        
        return self.children[key]
    
    def add_child(self, k):
        self.children[k] = Node(k)
        

