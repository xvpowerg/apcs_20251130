inArr = input().split()  #切割輸入字串

#轉型, 並將大於0的a b值轉換為1
a = 1 if(int(inArr[0])>0) else 0 
b = 1 if(int(inArr[1])>0) else 0
c = int(inArr[2])

#驗證a與b 以and、or、xor 運算結果是否為c
and_op = True if((a and b)==c) else False
or_op = True if((a or b)==c) else False
xor_op = True if((a != b)==c) else False

#運算符號運算結果為c時印出該運算符號
if(and_op):
    print('AND')
if(or_op):
    print('OR')
if(xor_op):
    print('XOR')
#三個運算符號均無法取得該結果列印"IMPOSSIBLE"
if(not(and_op or or_op or xor_op)):
    print('IMPOSSIBLE')
