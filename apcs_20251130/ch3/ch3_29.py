## 檢查所輸入的數是否為質數
#除了1 或自己能整除的數
num = int(input("請輸入數字"))
isPrimeNum = True
for i in range(2,num):
    if num % i == 0:
        isPrimeNum = False
        break
if isPrimeNum:
    print(num,"是質數")
else:
    print(num,"不是質數")
