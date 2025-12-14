#具名參數
def print_info(a,b=5,c=10):
    print("a:",a,"b:",b,"c:",c)
    
print_info(15,16,19)
print_info(18,c = 99)
#只要使用了具名參數之後的參數必須使用具名參數
print_info(b = 78,a = 65)
