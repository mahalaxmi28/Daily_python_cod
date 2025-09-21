num = 121
original = num
sum = 0
while num>0:
    rem = num%10
    sum = sum*10+rem
    num = num//10

print(sum)

if(sum == original):
    print(True)
else:
    print(False)