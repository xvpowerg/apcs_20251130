def func():
    global a #宣告a是外部的變數
    a += 1
    print("func a:",a)
a = 5
print("全域 a =",a)
func()
print("全域 a =",a)
