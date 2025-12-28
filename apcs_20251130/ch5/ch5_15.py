for i in range(1,5):
    print("Start i:",i)
    for k in range(1,4):
        print(i,"_",k,end=" ")
        if i == 2:
            break
    print()    
    print("End i:",i)
