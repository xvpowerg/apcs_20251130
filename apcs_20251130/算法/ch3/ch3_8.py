class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def add_front(self,item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        
link = Linked_list()
data = [5,15,25]
for n in data:
    link.add_front(n)
link.print_list()





    
