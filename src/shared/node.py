class node:
    """
    Represents a node. 
    A node is an object that has a data that is pointing to another node.
    """
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data