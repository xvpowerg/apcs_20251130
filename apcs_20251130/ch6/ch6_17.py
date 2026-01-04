poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉
'''
try:
    file = open("output2.txt","w")
    file.write(poem)
    file.flush()
    file.close()
    print("寫出成功")
except Exception as e:
    print("寫出失敗:",e)
