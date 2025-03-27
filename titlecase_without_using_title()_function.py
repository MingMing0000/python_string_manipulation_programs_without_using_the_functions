#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
#get string from user
#split the string into words
#use upper() and lower() to convert the first letter of each word to uppercase and the rest to lowercase
#join the words back to form the original string
#display the converted string

#get string from user
input_string = input('Enter a text to convert to title case: ')

#display the user input
print('Original text:', input_string)

#split the string into words
words = input_string.split()