#字典序
#不同大小寫 小寫大於大寫 相同大寫小寫a最小z最大
v1 = "a"
v2 = "A"
print(v1,">",v2,v1 > v2)
v1 = "x"
v2 = "z"
print(v1 ,"<",v2,v1 <v2)
v1 = "cDE"
v2 = "cdE"
print(v2,">",v1,v2 > v1)
v1 = "abcd"
v2 = "abcd"
print(v1,"==",v2,v1 == v2)

v1 = "abcc"
v2 = "abc"
print(v1,"<",v2,v1<v2)
