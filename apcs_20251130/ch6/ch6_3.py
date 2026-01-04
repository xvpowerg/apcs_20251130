import random

ans = random.randint(1,5)
print(ans)
#猜對顯示猜對
#猜錯沒滿3次顯示 猜錯
#猜錯滿3顯示遊戲結束
for i in range(1,4):
    guess = int(input("請猜一個數字1~5")) 
    if guess == ans:
        print("猜對")
        break
    elif i < 3:
        print("猜錯")
else:
    print("遊戲結束")
    

