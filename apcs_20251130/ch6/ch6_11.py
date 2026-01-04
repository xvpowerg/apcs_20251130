from calculator import calcBmi,getMessage

h = int(input("身高:"))
w = int(input("體重:"))

bmi = calcBmi(h,w)
message = getMessage(bmi)

print(f"BMI:{bmi:.2f}, {message}")
