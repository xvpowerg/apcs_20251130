"""
建立一個Student 類別
有姓名 成績
Ken 88
Vivin 99
Lucy 65
加入list並幫我排序
由小到大顯示list內容
"""
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name} {self.score}"
myList = []
st1 = Student("Ken",88)
st2 = Student("Vivin",99)
st3 = Student("Lucy",65)
myList.append(st1)
myList.append(st2)
myList.append(st3)
myList.sort(key=lambda st:st.score)
#https://docs.python.org/zh-tw/3/library/operator.html
for st in myList:
    print(st)
