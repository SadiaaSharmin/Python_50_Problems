#Find highest frequency character in a string
characters = "abcdefghijklmnopqrstuvwxyz"
string = str(input("Enter string: "))
for i in characters:
    c = string.count(i)
    if c>1:
        print(i,c)
