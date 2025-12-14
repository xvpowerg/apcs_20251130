#請寫一個程式，判斷輸入的整數為否為2或3的倍數

num = int(input("請輸入整數"))
if num % 2 == 0:
    print("是2的倍數",end="")
    if num % 3 == 0:
        print(",也是3的倍數")
else:
    if num % 3 == 0:
     print("是3的倍數")
    else:
     print("不是3與2的倍數")   
