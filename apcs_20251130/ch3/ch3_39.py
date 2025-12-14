def c2f(c):
    f = 9 / 5 * c + 32
    return f

while True:
   inStr = input("輸入攝氏溫度(輸入q離開):") 
   if inStr == 'q':
       print("結束")
       break
   tc = float(inStr)
   print(f"攝氏溫度{inStr}等於華氏溫度{c2f(tc):.2f}度")
    
