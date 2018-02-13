x = int(input("Enter a number: "))
if((x%10 == 0) and (x%50 == 0)):
    if(x%30 == 0):
        print("This number is divisible by 10, 50 and 30")
    else:
        print("This number is divisible by 10 and 50 but not 30")
