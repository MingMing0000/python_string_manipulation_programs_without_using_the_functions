#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
#have a string
#create algorithm to check if all characters are in uppercase
#use for loop to iterate through the string
#put condition to check if the character is in uppercase
#print the result

#create a string
string = input('Enter a text to check if all characters are in uppercase: ')
print('word:', string)

#create list of uppercase characters
uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
uppercase_count = 0

#check if each characters are in uppercase
for char in string:
    if char in uppercase_letters:
        uppercase_count += 1

#check if all characters are in uppercase
if uppercase_count == len(string):
    print("All characters are in uppercase")
else:
    print("Not all characters are in uppercase")