
"Circular linked list using doubly linked list"


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class CLL:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def insert_at_start(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            new_node.next = self.head
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node



    def search(self,data):
        
        if self.head is None:
            print("List is empty!!")
        else:
            temp = self.head
            while True:
                if temp.data ==data:
                    return temp
                temp = temp.next

                if temp == self.head:
                    break
                return None
            

    def insert_after(self,node,data):
        new_node = Node(data)

        if self.head is None:
            print("List is empty!")

        elif node.next == self.head:
            self.insert_at_last(data)

        else:
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
            new_node.prev = node

    def println(self):
        temp = self.head
        
                    

