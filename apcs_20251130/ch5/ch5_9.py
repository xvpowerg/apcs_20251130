myList = [("Ken",75),("Vivin",83),("Vivin",74),("Ken",85),("Iris",96),("Iris",34)]
dataDict = {}

for name,score in myList:
    if name in dataDict:
        dataDict[name].append(score)
    else:
        dataDict[name] = [score]

print(dataDict)
name = input("輸入姓名")#輸入姓名 查成績 如無對應的成績 顯示查無此人
if name in dataDict:
    print(dataDict[name])
else:
    print("查無此人")
