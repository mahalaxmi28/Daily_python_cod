#adding and removing a elemnt in a set

s1 ={1,2,3,4,5};
print(s1)

s1.add(6)
s1.remove(2)
print(s1)

#finding union and INtersection in Set
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))
print(A.union(B))

# finding subset
x = {1,2,3}
y= {1,2,3,4,5}

# s2 = y.union(x)


# if(y == s2):
#     print(True)
# else:
#     print(False)

print(x.issubset(y))

#removing duplicates in a list using set
numbers = [1, 2, 2, 3, 4, 4, 5]
numbers = set(numbers)
print(numbers)

