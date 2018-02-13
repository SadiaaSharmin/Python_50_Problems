#Count vowels and consonants in a string
string = str(input("Enter string: "))
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
num_of_v = 0
num_of_c = 0
for i in string:
    if(i in vowels):
        num_of_v = num_of_v +1
    elif(i in consonants):
        num_of_c = num_of_c +1
print("Vowels: ",num_of_v, "Consonants: ",num_of_c)
