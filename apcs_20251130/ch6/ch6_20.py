import csv
class Student:
    def __init__(self,name,score=0):
        self.name = name
        try:
            self.score = float(score)
        except:
            pass
    def __str__(self):
        return f"{self.name} {self.score}"
    def __lt__(self,other):
        return self.score < other.score
file = open("data2.csv","r")
csvCursor = csv.reader(file)
stList = []
for row in csvCursor:
    #print(row[0],row[2])
    st = Student(row[0],row[2])
    stList.append(st)
file.close()
#Student 物件有 姓名 成績
#以上一群Student存於List
#並根據 成績對List作排序
stList.sort()
for st in stList:
    print(st)




