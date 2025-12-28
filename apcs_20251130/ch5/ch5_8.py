scores={'Ch':100,'En':80, 'Ma':95, 'Na': 90}
print(scores)
del scores["Ch"]
print(scores)

delKey = "T1"
if delKey in  scores:
    del scores[delKey]
