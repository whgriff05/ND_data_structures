class Dictionary:
    def __init__(self):
        self.contents = {}

    def __contains__(self, word):
        return True if word in self.contents.keys() else False
    
    def append(self, word):
        if word not in self:
            self.contents[word] = 1
            return True
        else:
            return False