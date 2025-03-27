#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
#get input from user
#subtract the length of string to the length of the string that will be justified
#add space characters to the end of the string
#display the justified string

#get string from user
input_string = input('Enter a text: ')

#get length of string user wants
string_length = int(input('How many characters do you want the text to be: '))

#display the user input
print(f'Original text:"{input_string}"')
print(f'Length of text to be outputted: {string_length}')

#subtract the length of string to the length of the string that will be justified
space_length = string_length - len(input_string)

#add space characters to the end of the string
output_string = input_string + (' ' * space_length)

#display the justified string
print(f'Justified text: "{output_string}"') #I have added double quotes to show that there are spaces at the end of the string.