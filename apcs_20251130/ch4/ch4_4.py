def sumFunc(*values):
    result = 0
    for v in values:
        result += v
    return    result 
def sumFunc2(a,b,*values):
    result = a + b
    for v in values:
        result += v
    return result    

#可傳入n筆數字 或不傳
#幫我加總回傳
#顯示數值        
ans = sumFunc()
print(ans)
ans2 = sumFunc(1,2,3,4)
print(ans2)


#限制至少傳2個參數
ans = sumFunc2(1,2)
print(ans)
ans = sumFunc2(1,2,3,4,5,6)
print(ans)
