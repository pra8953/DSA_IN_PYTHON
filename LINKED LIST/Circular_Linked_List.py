
'''Circular linked list using singly linked list'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Cll:
    def __init__(self):
        self.tail = None
    
    def is_empty(self):
        return self.tail is None
    
    def insert_at_start(self,data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node

        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    def insert_at_last(self,data):
        new_node = Node(data)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    def search(self, data):
        if self.tail is not None:
            temp = self.tail.next  # Start from head node
            while True:
                if temp.data == data:
                    return temp  # Return the node if data matches
                temp = temp.next
                if temp == self.tail.next:  # If we are back to the head node, stop
                    break
            return None  # Data not found in the list
        else:
            print("List is empty!!")
            return None



    def insert_after(self,node,data):
        new_node = Node(data)
        if self.tail is None:
            print("List is empty!!")
        elif node is None:
            print("Enter valid Node")

        elif node == self.tail:
            new_node.next= self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = node.next
            node.next = new_node 

    def delete_first(self):
        if self.tail is None:
            print("List is empty ")
        elif self.tail.next == self.tail:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next

    def delete_last(self):
        if self.tail is None:
            print("List is empty ")
        elif self.tail.next == self.tail:
            self.tail = None

        else:
            # pass
            temp = self.tail.next
            while temp.next != self.tail:
                temp = temp.next

            temp.next = self.tail.next
            self.tail = temp

    def delete_item(self,data):

        if self.tail is None:
            print("List is empty!!")

        elif self.tail.next.data == data:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next
        else:
            temp = self.tail.next
            while temp.next != self.tail:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next

            if temp.next == self.tail:
                if temp.data == data:
                    self.delete_last()
                    return
            print("Item not Found 404!")
    
    # def print_list(self):

    #     if self.tail is None:
    #         print("List is empty!!")
    #     else:
    #         temp = self.tail.next
    #         while True:
    #             print(temp.data,end="->")
    #             if temp.next == self.tail.next:  # If we are back to the head node, stop
    #                 break
    #             temp = temp.next
            
    #         print("None")
    
    def print_list(self):
        if self.tail is None:
            print("List is empty!!")
        else:
            temp = self.tail.next  # Start from head node
            while temp != self.tail:
                print(temp.data, end="->")
                temp = temp.next
            # Print the last node (self.tail)
            print(temp.data, end="->")
            print("None")
    

l = Cll()
l.insert_at_start(3)
l.insert_at_start(2)
l.insert_at_start(1)
l.insert_at_last(6)
l.insert_at_last(16)
# l.insert_at_last(7)
# l.insert_at_last(8)
# print(l.search(81))
l.insert_after(l.search(6),"RAM")
l.delete_item(116)
l.print_list()