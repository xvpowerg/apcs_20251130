s1 = input("請輸入國文成績")
s2 = input("請輸入數學成績")
s3 = input("請輸入英文成績")

total = int(s1) + int(s2) + int(s3)
print("總成績:",total)
print("平均分數:",round(total/3,2) )
