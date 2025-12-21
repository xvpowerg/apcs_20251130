strList = ["12","25","76"]
#請寫一個函數將strList內容都轉換為整數
def listValueToInt(myList,myfunc):
    result = []
    for i in myList:
        result.append(myfunc(i))    
    return result

ans = listValueToInt(strList,int)

for v in ans:
    print(v,type(v))
