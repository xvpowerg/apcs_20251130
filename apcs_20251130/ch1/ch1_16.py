name="小明"
age = 12
msg = name+"今年"+str(age)+"歲"
print(msg)#小明今年12歲
#%d表填入整數 %s表示要填字串 %f表示要填浮點數

msg2 = "%s今年%d歲"%(name,age)
print(msg2)
msg3 = f"{name}今年{age}歲"#f 表示{}內的是變數
print(msg3)
