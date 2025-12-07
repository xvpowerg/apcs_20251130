#身分證字號 第二位如果是1,2顯示TRUE 其他顯示False
#A123456789
myId = input("輸入身分證")
print(myId[1] == "1" or myId[1] == "2" ) 
