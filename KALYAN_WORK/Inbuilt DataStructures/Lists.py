#creating a list of fruits and printing first and last element
fruits = ["bannana","Apple","Watermelon","Cherry","Mango"]
print(fruits[0],fruits[-1])


# changing first value to Mango and last value to Banana
fruits[0] = "Mango"
fruits[-1] = "Banana"

print(fruits)


#remove a element from the list
fruits.remove("Watermelon")
print(fruits)


#Slicing: printing first two elements and last two elements
print(fruits[0:2])
print(fruits[-2:])


#sum() function in list
nums = [1,2,3,4,5]
print(sum(nums))

#max() and min() functions in list
print(max(nums),min(nums))

#reverse a list without slicing

for i in range(0,len(nums)//2):
    temp = nums[i]
    nums[i] = nums[len(nums)-i-1]
    nums[len(nums)-i-1] = temp

print(nums)