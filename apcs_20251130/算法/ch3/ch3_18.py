class Queue:
    def __init__(self,capacity):
        self.queue = []
        self.capacity =capacity
    def isEmpty(self):
        return self.size() == 0
    def isFull(self):
        return self.size() == self.capacity
    def enqueue(self,data):
        if self.isFull():
            print(f"{data}已滿")
            return
        self.queue.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("序列為空")
            return None
        return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)

    
queue = Queue(3)
pepole = ["Amy","David","Sean","Vivin"]

for p in pepole:
    queue.enqueue(p)

for i in range(3):
    item = queue.dequeue()
    print(item)



