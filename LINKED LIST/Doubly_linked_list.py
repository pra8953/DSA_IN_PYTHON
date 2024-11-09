class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #this method tells list is empty or not
    def is_empty(self):
        return self.head is None
    
    # This method add Node at the start of list
    def insert_at_start(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.next = self.head
            self.head.prev = new_node
            self.head = new_node


    # This method add Node at the last in list
    def insert_at_last(self,data):
        new_node = Node(data)
        

