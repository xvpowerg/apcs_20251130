import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

val=0
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
showData(data)
while True:
    value = int(input("請輸入搜尋值(1~100),-1離開"))
    if value == -1:
        break
    for i in range(50):
        if data[i] == value:
            print(f"{value}在第{i+1}位置")
            break
    else:
        print(f"{value}找不到")
