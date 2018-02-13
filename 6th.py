#Find maximum number between three numbers
num1 = float(input("Enter 1st number: "))
num2 = float(input(" Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

if(num1 >= num2) and (num1 >= num3):
    maximum = num1
elif(num2 >= num1) and (num2 >= num3):
    maximum = num2
else:
    maximum = num3

print("Maximum number between",num1,",",num2,"and",num3,"is" ,maximum)
