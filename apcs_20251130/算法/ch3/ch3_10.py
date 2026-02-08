class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return f"{self.data}"
class Linked_list:
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def add(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newNode
    def indexOf(self,value):
        ptr = self.head
        i = 0
        while ptr:
            if ptr.data == value:
                break
            ptr = ptr.next
            i+=1
        else:
            i = -1
        return i    
import random    
link =Linked_list()
for i in range(5):
    link.add(random.randint(1,10))
link.print_list()
target = random.randint(1,10)
i = link.indexOf(target)
if i>=0:
    print(f"index:{i} target:{target} 存在")
else:
    print(f"index:{i} target:{target} 不存在")
    



