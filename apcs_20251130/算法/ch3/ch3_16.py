class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def push(self,item):
        newNode = Node(item)
        newNode.next = self.top
        self.top = newNode
    def pop(self):
        if self.isEmpty():
            print("堆疊為空")
            return None
        else:
            ptr = self.top
            self.top = ptr.next
            return ptr.data
        
    def size(self):
        ptr = self.top
        count = 0
        while ptr:
            ptr = ptr.next
            count += 1
        return count    
        

stack = StackLL()
fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
for f in fruits:
    stack.push(f)
print(f"size:{stack.size()}")

while not stack.isEmpty():
    print(stack.pop())
