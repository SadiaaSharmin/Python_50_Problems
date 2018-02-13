string = str(input("Enter string: "))
rev_string = reversed(string)

if list(string) == list(rev_string):
    print(string,"is palindrome")
    
else:
    print(string, "is not palindrome")
             
