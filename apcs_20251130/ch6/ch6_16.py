poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉
'''
try:
    print(poem,file=open("output.txt","w"),flush=True)
    print("寫入完成")
except Exception as e:    
    print("資料寫出失敗:",e)
