#Even Odd number check using Bitwise Operator
num = int(input("Please enter a number : "))

if(num&1 ==1):
    print(num, "is Odd")
    
else:
    print(num, "is Even")
