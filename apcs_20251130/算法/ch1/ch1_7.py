def test1(num):
    print("Start:",num)
    if num < 5:
        print(num,end=" ")
        test1(num + 1)
    print("End:",num)
test1(1)
