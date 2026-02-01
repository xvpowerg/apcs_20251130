scores = [87,66,90,65,70]
score_sum = 0
counts = len(scores)
score_max = 0
score_min = 100
for i in range(counts):
    print(f"第{i}筆學生分數{scores[i]}")
    score_sum +=  scores[i]
    if scores[i] > score_max:
        score_max = scores[i]
    if scores[i] < score_min:
        score_min = scores[i]
        
print(f"總分:{score_sum}")
print(f"平均分:{score_sum/counts:.2f}")
print(f"最高分:{score_max}")
print(f"最低分:{score_min}")
