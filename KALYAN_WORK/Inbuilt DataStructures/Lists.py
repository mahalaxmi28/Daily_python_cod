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

# for i in range(0,len(nums)//2):
#     temp = nums[i]
#     nums[i] = nums[len(nums)-i-1]
#     nums[len(nums)-i-1] = temp

nums.reverse()

print(nums)

# count the occurences in a list
numbers = [1,2,3,4,5,2,3,2]
# count = 0
# for i in range(0,len(numbers)):
#     if(numbers[i] == 2):
#         count = count+1

print(numbers.count(2))

#checking for a element that exist in list or not
bool = False
for i in range(0,len(fruits)):
    if(fruits[i] == "Banana"):
        bool = True
print(bool)


#printing a element in matrix using indexing
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[1][1])