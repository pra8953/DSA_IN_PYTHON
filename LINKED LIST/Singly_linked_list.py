"Singly linked list"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0


    # This method checks list is empty or not and return value in forms of True or False
    def is_empty(self):
        return self.head is None
    
    # This method add Node start of list 
    def insert_at_first(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count +=1
    

    # This method add Node at last of list
    def insert_at_last(self,data):
        new_node = Node(data)
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node
        self.count +=1

    # This method search item in list and return Node
    def search(self,data):
        if self.head is None:
            print("List is empty!!")
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    return temp
                temp = temp.next
            print("Node not found!!")
            return None
        
    #This method add new node in list at particular provided node
    def insert_at_node(self,node,data):
        
       
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.count +=1
   

    # This method add node at the particular index and index consider at 1
    def insert_at_index(self,index,data):
        new_node = Node(data)
        if index<1:
            print("Bhai ish function main indexing 1 sey start ho rha hai tho tum 1 or more index dalo")

        elif index>self.count and index!=1:
            raise IndexError("Index value not sufficent")
        
        elif index==1:
            new_node.next = self.head
            self.head = new_node
            self.count +=1

        else:
            temp = self.head
            for i in range(1,index-1):
                temp =  temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.count +=1
    

    # This method delete first node of list
    def delete_at_first(self):
        if self.head is None:
            print("List is empty!!")
        else:
            self.head = self.head.next

    # This method delete last node of list
    def delete_at_last(self):
        temp = self.head
        if self.head is None:
            print("List is empty!!")
        elif self.head.next is None:
            self.head = None
        else:
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None


    def delete_item(self, data):
        if self.head is None:
            print("List is empty !!")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    return  # Item found and deleted, exit the function
                temp = temp.next
            print("Item not found in the list")

    

    

    # This method print list
    def display_list(self):
        if self.head is None:
            print("List is empty!!")
            
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end="->")
                temp = temp.next
            print(None)


            
        

sll = SinglyLinkedList()
# sll.insert_at_index(0,5)
sll.insert_at_first(10)
sll.insert_at_index(1,6)
sll.insert_at_first(101)
sll.insert_at_node(sll.search(6),"RAM")
# sll.delete_item(101)
# sll.delete_item(6)
sll.delete_item(10)

# sll.delete_item(10)
# sll.delete_at_node("RAM")
# sll.delete_at_first()
# sll.delete_at_last()


# sll.insert_at_index(2,50)
# sll.insert_at_index(3,55)
# sll.insert_at_index(19,788)
sll.display_list()