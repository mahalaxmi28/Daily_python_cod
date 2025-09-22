person ={
    "name" : "Kalyan",
    "age" : 20,
    "branch" : "C.S.E"

}

print(person["name"])
print(person["age"])

person["roll no"] = 101
print(person)

del person["branch"]

print(person)


fruits = {"apple": 50, "banana": 20, "cherry": 75}

fruits["banana"] = fruits["banana"]+5
print(fruits)

for i,j in fruits.items():
    print(i,j)