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
           new_node.next = self.head
           self.head.prev =new_node
           self.head = new_node


    # This method add Node at the last in list
    def insert_at_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    
    # This method search node exits or Not
    def search(self,data):

        temp = self.head
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None
    
    #this method insert a new node after a Node
    def inseart_after_node(self,node,old_data,new_data):
        if self.search(old_data):
            new_node = Node(new_data)
            new_node.next = node.next
            if node.next is not None:
                node.next.prev = new_node
            node.next = new_node
            new_node.prev = node
        else:
            print("Node doesn't exits in list")
        

    # delete first node of linked list
    def delete_at_first(self):
        if self.head is None:
            print("List is empty!! can't delete")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_last(self):
        if self.head is None:
            print("List is empty!! can't delete")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next.prev = None
            temp.next = None

    def delete_item(self,data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    if temp.next is not None:
                        temp.next.prev = temp
                    return
                temp = temp.next
            print("Item not in list")


    
    def print_list(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.data,end="->")
                temp = temp.next
            print(None)
        else:
            print("List is empty!!")




d = DoublyLinkedList()
d.insert_at_start(8)
d.insert_at_start(7)
d.insert_at_last(10)
d.inseart_after_node(d.search(7),7,"RAM")
d.insert_at_start(1000000)
# d.delete_at_last()
d.delete_item('RM')
d.print_list()
    



