class Node:
    def __init__(self, key=None):
        self.key = key
        self.children = {}

    def has_children(self):
        return False if len(self.children.items()) == 0 else True
    
    def __getitem__(self, key):
        if key not in self.children:
            raise KeyError
        
        return self.children[key]
    
    def __setitem__(self, key, value):
        self.children[key] = value

