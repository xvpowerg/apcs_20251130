cars = ['Honda','Toyota','Ford','BMW']
print(cars)
cars.remove("Toyota")
print(cars)
reValue = "Ford"
if reValue in cars:
    cars.remove(reValue)
    print(f"已刪除{reValue}")
else:
    print(f"無法刪除{reValue}")
