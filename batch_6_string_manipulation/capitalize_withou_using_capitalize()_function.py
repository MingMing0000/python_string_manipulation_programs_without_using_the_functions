#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
#get string from user
#use upper() and lower() to convert the first letter of the string to uppercase and the rest to lowercase
#display the converted string

#get string from user
input_string = input('Enter a text to convert to capitalize: ')

#display the user input
print('Original text:', input_string)

#use upper() and lower() to convert the first letter of the string to uppercase and the rest to lowercase
output_string = input_string[0].upper() + input_string[1:].lower()

#display the converted string
print('Capitalized text:', output_string)