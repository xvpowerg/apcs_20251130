def rotate(matrixB):
    matrixA = []
    r = len(matrixB)
    c = len(matrixB[0])
    for i in range(c-1, -1, -1):
        row = []
        for j in range(r):
            row.append(matrixB[j][i])
        matrixA.append(row)
    return matrixA

def flip(matrixB):
    matrixA = []
    r = len(matrixB)
    for i in range(r-1, -1, -1):
        matrixA.append(matrixB[i])
    return matrixA

#讀取資料 R C M：列 欄 操作次數
inStrs = input().split(' ')
R = int(inStrs[0])
C = int(inStrs[1])
M = int(inStrs[2])

#讀取R次，切割為C筆資料，加入二維List
matrix = []
for i in range(R):
    temp = input().split(' ')
    rList = []
    for j in range(C):
        rList.append(int(temp[j]))
    matrix.append(rList)
    
#讀取操作，切割為 M 筆操作
ops = input().split(' ')

#操作資料 : 0->旋轉(rotate) / 1->翻轉(flip)
#反向順序
for k in range(M-1, -1, -1):
    op = int(ops[k])
    if(op==0):
        matrix = rotate(matrix)
        #print('rotate', matrix)
    elif(op==1):
        matrix = flip(matrix)
        #print('flip', matrix)

#輸出 R C
Rr = len(matrix)
Rc = len(matrix[0])
print(Rr, Rc)

#輸出二維List：輸出R次，每列有C筆資料
for i in range(Rr):
    print(' '.join(str(matrix[i][j]) for j in range(Rc)))
   
