age = 20;
if(age>=18):
    print("you can vote")

# check given number is odd or even

num = 8
if(num%2 == 0):
    print(num," is even number")
else:
    print(num," is odd number")

# check the given year is leap year or not

year = 100

if((year % 400 ==0) or (year % 4== 0 and year%100!=0)):
   print(year," is a leap year")
else:
    print(year," is not a leap year")


for i in range(1,6):
    print(i)