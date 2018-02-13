num = int(input("Please Enter the Range Number: "))
i = 0
n1 = 0
n2 = 1
while (i < num):
    if(i <=1):
        n3 = i
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(n3)
    i = i + 1
