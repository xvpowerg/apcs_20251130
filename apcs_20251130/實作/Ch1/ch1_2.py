#讀取輸入後切割
inArr = input().split()
#轉型
numArr = []
for s in inArr:
    numArr.append(int(s))
#排序
numArr.sort()
a = numArr[0]
b = numArr[1]
c = numArr[2]
print(' '.join(str(x) for x in numArr))
#驗證三角形
if(a + b <= c):
    #a + b <= c ：無法構成三角形，印出 No
    print('No')
else:
    #a + b > c    
    if(a**2+b**2<c**2):
        #a*a + b*b < c*c ：構成鈍角三角形，印出 Obtuse
        print('Obtuse')    
    elif(a**2+b**2==c**2):
        #a*a + b*b = c*c ：構成直角三角形，印出 Right
        print('Right')
    else:
        #a*a + b*b > c*c ：構成銳角三角形，印出 Acute
        print('Acute')
