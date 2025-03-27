#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
#get input from user
#subtract the input length of string to the length of the string that will be justified
#divide the space length by 2
#add space characters to the beginning and end of the string
#display the justified string

#get string from user
input_string = input('Enter a text: ')

#get length of string user wants
string_length = int(input('How many characters do you want the text to be: '))

#display the user input
print(f'Original text:"{input_string}"')
print(f'Length of text to be outputted: {string_length}')

#subtract the input length of string to the length of the string that will be justified
space_length = string_length - len(input_string)

#divide the space length by 2
space_length = space_length // 2