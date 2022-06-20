import shared.node as shared
class linked_list:
    """
    Python implementation of LinkedList data structure.
    """
    def __init__(self):
        self.root_node = None

    def add(self, data):
        """
        Adds data to the linked list
        """
        new_node = shared.node(data)

        if self.root_node is None:
            self.root_node = new_node
        else:
            _root = self.root_node
            while _root.next_node is not None:
                _root = _root.next_node

            _root.next_node = new_node

    def insert_at(self, data, index):
        if self.root_node is None:
            return None

        new_node = shared.node(data)

        if self.root_node is None:
            self.root_node = new_node
        elif index == 0:
            temp_node = self.root_node
            self.root_node = new_node
            self.root_node.next_node = temp_node
        else:
            left_node = self.get_node_at(index - 1)
            if left_node is None:
                raise IndexError("IndexError " + str(index))
            
            nodeAtIndex = left_node.next_node
            left_node.next_node = new_node
            new_node.next_node = nodeAtIndex
    
    def remove(self, data):
        _root = self.root_node
        if _root is None:
            return

        previous_node = self.root_node
        while _root is not None:
            if _root.data == data:
                previous_node.next_node = _root.next_node
                return data

            previous_node = _root
            _root = _root.next_node
        
        return None
    
    def search(self, search_data):
        n_node = self.root_node
        while n_node is not None:
            if n_node.data == search_data:
                return search_data

            n_node = n_node.next_node
        
        return None

    def get_node_at(self, index):
        count = 0
        n_node = self.root_node
        while n_node is not None:
            if count == index:
                break

            n_node = n_node.next_node
            count += 1
        
        return n_node

    def to_array(self):
        arr = []
        s_node = self.root_node
        while s_node is not None:
            arr.append(str(s_node.data))
            s_node = s_node.next_node
        
        return arr

    def length(self):
        return len(self.to_array)

    def __add__(self, other):
        for item in other.to_array():
            self.add(item)
        
        return self
    
    def __eq__(self, data):
        return  self.search(data) != None

    def __repr__(self):
        return ",".join(self.to_array())

if __name__ == '__main__':
    ll = linked_list()
    ll.add(2)
    ll.add(1)
    ll.add(0)
    ll.add(5)
    ll.add(6)
    ll.add(30)
    ll.add(1000)
    print(ll)
    ll.insert_at(300, 3)
    print(ll)
    print("Searching 2")
    print(ll.search(2))
    print('before add', ll)

    l2 = linked_list()
    l2.add(900)

    l3 = ll + l2
    print(l3)
    print(ll)