#Whether a string is palindrome or not
string = str(input("Enter string: "))
if(string==string[::-1]):
    print(string, "is palindrome")
else:
    print(string, "is not palindrome")
