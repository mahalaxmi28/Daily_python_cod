fruits = ("banana","watermelon","apple","orange","pappaya")

print(fruits[1],fruits[3])

#unpacking a tuple
numbers = (1,2,3,4,5)
a,b,c,d,e = numbers
print(a)
print(b)
print(c)
print(d)
print(e)

#occurence of number
nums = (1,2,3,3,5,7,3,2)
print(nums.count(3))

#swapping two tuples
t1 = (1,2,3)
t2 = (4,5,6)

temp = t1
t1 = t2
t2 = temp
print(t1,t2)


# sum and avg of a tuple by converting it into a list
t3 = (1,2,3,4,5)
l1 = list(t3)
print(sum(l1),sum(l1)/len(l1))


a,*b,c = t3
print(a,b,c)


