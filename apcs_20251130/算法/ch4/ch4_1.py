class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"{self.title}:{self.author}:{self.price}"
class BookStack:
    def __init__(self,capacity):
        self.my_stack = [None]*capacity
        self.top = -1
        self.capacity = capacity
    def push(self,data):
        if self.isFull():
            print("書箱已滿")
        else:
            self.top += 1
            self.my_stack[self.top] = data            
    def pop(self):
        if self.isEmpty():
            print("書箱為空")
            return None
        else:
            data = self.my_stack[self.top]
            self.my_stack[self.top] = None
            self.top -= 1
            return data        
    def size(self):
        return self.top+1
    def isEmpty(self):
        return self.size() <= 0
    def isFull(self):
        return self.size() >= self.capacity
    def printStack(self):
        for b in self.my_stack:
            print(b,end=",")
        print()    

        
books = [Book("Java","Ken",500),
         Book("C#","Iris",600),
         Book("Pythn","Joy",800),
         Book("Golan","Sean",400)]
bookStack = BookStack(3)
for b in books:
    #print(b)
    bookStack.push(b)
    bookStack.printStack()
print("="*20)
for i in range(4):
    print(bookStack.pop())
    
