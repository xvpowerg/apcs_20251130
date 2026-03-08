def showdata(data_list):
    for i in range(len(data_list)):
        print('%3d' %data_list[i],end='')
    print()

data=[16,25,39,63,27,12,8,45]
print('選擇排序法:原始資料為：')
showdata(data)

n = len(data)

for i in range(n-1):
    midIdx = i
    for j in range(i+1,n):
        if data[j] < data[midIdx]:
              midIdx = j
    data[i],data[midIdx] = data[midIdx],data[i]
    showdata(data)
print("排序完成:")    
showdata(data)    
              
