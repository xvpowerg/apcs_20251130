#是迴文 或 不是迴文
str1 = input("請輸入文字")
if str1 == str1[::-1]:
    print("是迴文")
else:
    print("不是迴文")
