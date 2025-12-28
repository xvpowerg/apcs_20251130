scores = {"Ch":100,"En":80,"Ma":95}
print(scores)
add_dic = {"So":90}
scores.update(add_dic)#沒有key 新增
print(scores)
add_dic = {"Ma":0}
scores.update(add_dic)#有key 就修改
print(scores)
scores.update({"Ch":99,"En":75})
print(scores)
scores["Ma"] = 85#有key 就修改
print(scores)
scores["PM"] = 77#沒有key 新增
print(scores)
