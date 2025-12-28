class  Fruit:
    def __init__(self,name,price):
        self.name= name
        self.price = price
        print(f"{name}:{price}建立")
    def printInfo(self):
        print(self.name,self.price)
    def __del__(self):
        print(self.name,":",self.price,"刪除了")
f1 = Fruit("Apple",25)
f3 = Fruit("Cherry",12)
f1.printInfo()
f3.printInfo()
del f1
del f3
