poem = '''床前明月光X
疑是地上霜X
舉頭望明月X
低頭思故鄉X
'''
try:
    with open("output3.txt","a") as f:#自動關閉
        f.write(poem)
    print("完成")
except Exception as e:
    print("寫出失敗:",e)
