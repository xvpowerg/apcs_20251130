myList = ["Ken","Vivin","Lucy","Joy"]
msg = ""

for i in range(len(myList)):
    s = myList[i]
    if i < len(myList) - 1:
        msg += s+","
    else:
        msg += s

print(msg)#Ken,Vivin,Lucy,Joy
