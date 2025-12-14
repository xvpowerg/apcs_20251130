result = {"David":0,"Amy":0,"Sean":0}
for i in range(5):
    vote = input("投票給:")
    if vote not in result:
        print("無效票")
        continue
    result[vote] += 1

for key in result:
    print(key,f"{result[key]}票數")
