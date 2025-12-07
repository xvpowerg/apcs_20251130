height = float(input("身高單位公分"))
weight = int(input("體重單位公斤"))
bmi = weight / (height/100) ** 2
print(f"bmi為:{bmi:.2f}")
