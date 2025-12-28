def getResult(s):
    if  60 <= s <= 100:
        return "及格"
    elif s < 60 and s >= 0:
        return "不及格"
    else:
        #return "錯誤的成績"
        raise OverflowError("錯誤的成績")    
print(getResult(-1))
print("完成")
    #及格 >= 60 <= 100
    # 不及格< 60 >= 0
    #顯示錯的成績
