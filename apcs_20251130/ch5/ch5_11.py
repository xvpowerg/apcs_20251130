num1 = 10
num2 = 0
names = ["Joy","Iris"]
try:
 print(num1/num2)
 print(names[2])
except ZeroDivisionError :    
 print("ZeroDivisionError")
except IndexError:
 print("IndexError")   

print("完成")
