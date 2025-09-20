input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")


if(operator == '+'):
    print("sum is: ",(input1+input2))
elif(operator == '-'):
    print("difference is: ",(input1-input2))
elif(operator == '*'):
     print("Multipilcation is: ",(input1*input2))
elif(operator =='/'):
    if(input2 ==0):
        print("Division by zero not allowed")
    else:
        print("Division is: ",input1/input2)
else:
    print("Invalid oprator")
