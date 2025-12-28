class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
    def __len__(self):
        return self.x**2 +self.y**2
    def __lt__(self,other):
        return len(self) < len(other)
p1 = Point(2,3)
p2 = Point(-1,2)
print(len(p1))
print(p1 < p2)
myList = [p1,p2]
myList.sort()
for v in myList:
    print(v)

