a = 5
def func():
    a = 10#在func內新宣告了一個a
    print("func():a=",a)

print("全域:a =",a)
func()
print("全域:a =",a)
