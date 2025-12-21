def personInfo(name,age,**other):
    print("=====info====")
    print("name:",name)
    print("age:",age)
    for key in other:
        print(key,":",other[key])

personInfo("Sean",40)
personInfo("David",35,phone="0920886552",company="IBM")
personInfo(name="Amy",age = 28,email="amy@gamil.com")
