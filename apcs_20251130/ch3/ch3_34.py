def show_for(s,e):
    for i in range(s,e+1):
        if i != e:
            print(i,end = " ")
        else:
            print(i,end = "")
    print()        
show_for(2,10)#2 3 4 5 6 7 8 9 10
show_for(5,8)#5 6 7 8
