## BMI 計算後分析
def calcBMI(h,w):
    return w / ( (h/100) ** 2)

def diagnose(bmi):
    result = "錯誤的數值"
    if bmi > 30:
        result = "胖胖"
    elif bmi > 25:
        result = "過重"
    elif bmi > 18.5:
        result = "正常"
    elif bmi > 0:
        result = "過輕"
    return result

heihgt = float(input("身高"))
weight = int(input("體重"))
bmi = calcBMI(heihgt,weight)
print(f"bmi:{bmi:.2f} {diagnose(bmi)}")

