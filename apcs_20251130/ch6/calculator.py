pi = 3.14159
def calcArea(r):
    return pi * r *ｒ

def toF(tempC):
    return 9/5 * tempC + 32

def calcBmi(h,w):
    return w / (h / 100) ** 2

def getMessage(bmi):
    if bmi <= 18.5:
        mesg = "過輕"
    elif 25 >bmi > 18.5:
        mesg = "正常"    
    elif bmi >= 25 and bmi < 30:
        mesg = "過重"
    elif bmi > 30:
        mesg = "胖胖"
    return mesg  
        
