scores = [ [50,60,70,0,0],
           [30,40,50,0,0],
           [70,80,90,0,0],
           [66,77,88,0,0],
           [22,33,44,0,0]]

for i in range(len(scores)):
    sSum = 0
    for j in range(3):
        sSum += scores[i][j]
        if scores[i][j] < 60:
            scores[i][4] += 1
    scores[i][3] = sSum / 3

subjs = [[0] * 3 for i in range(2)]
for x in range(3):
    subjSum = 0
    for y in range(5):
        subjSum += scores[y][x]
        if scores[y][x] < 60:
            subjs[1][x] += 1
    subjs[0][x] = subjSum / 5
    
for s in subjs:
    print(s)
