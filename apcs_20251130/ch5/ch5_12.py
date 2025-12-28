myList = [("Ken",80),("Joy",75),("Lucy",65)]
#我要輸出總成績
#學姓名與成績
total = 0

try:
    while True:
       name,score = myList.pop()
       total +=  score
       print(f"{name}:{score}")
except:
    pass

   
print(f"總成績:{total}")
