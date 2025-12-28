scores={'Ch':100,'En':80, 'Ma':95, 'Na': 90}
print(scores)
ch_score = scores["Ch"]
print("ch_score:",ch_score)
searchKey = "T1"
if searchKey in scores:
    T1 = scores["T1"]
    print("T1:",T1)

ch_score = scores.get("Ch")
print("Ch:",ch_score)
t2_score = scores.get("T2",-1)
print("t2_score:",t2_score)
