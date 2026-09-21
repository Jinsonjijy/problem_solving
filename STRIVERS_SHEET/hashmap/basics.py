hashmap=dict(name="jinson",age=22,location="kareepra")
hashmap1={}
print(len(hashmap))
for val in hashmap:
    print(hashmap[val])
cars={
    "company":"ford",
    "model":"mustang",
    "year":"1989",
    "mileage":"16kmpl",
}
for car in cars:
    print(car)

print(cars.get("mileage"))
cars.pop("mileage")
print(cars)
cars1=cars.copy()
cars1.pop("model")
print(cars)
cars.clear()
print(cars)
# del cars
# print(cars)