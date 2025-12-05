from node import Node

class Trie:
    def __init__(self):
        self.head = Node("*")

    def __contains__(self, word):
        current_node = self.head
        for letter in word:
            if current_node.get_child(letter) is None:
                return False
            current_node = current_node.get_child(letter)

        if current_node.get_child(0) is None:
            return False

        return True

    def append(self, word):
        if word not in self:
            current_node = self.head
            for letter in word:
                if current_node.get_child(letter) is None:
                    current_node.add_child(letter)

                current_node = current_node.get_child(letter)

            if current_node.get_child(0) is None:
                current_node.add_child(0)

            return True
        else:
            return False
        

