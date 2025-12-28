class Student:
    def __init__(self,name,score=0):
        self.name = name
        self.score =score
    def printInfo(self):
        print(self.name,self.score)
        
st1 = Student("Joy",85)
print(st1.name,st1.score)
st1.printInfo()
st2 = Student("Iris",77)
st2.printInfo()
#Iris 77
