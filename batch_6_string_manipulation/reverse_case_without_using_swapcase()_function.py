#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
#get string from user
#use ASCII to convert the characters to uppercase or lowercase
#display the converted string

# get string from user
input_string = input('Enter a text to reverse case: ')

#display the user input
print('Original text:', input_string)

output_string = ''
# use ASCII to convert the characters to uppercase or lowercase
for char in input_string:
    if 65 <= ord(char) <= 90:
        output_string += chr(ord(char) + 32)
    elif 97 <= ord(char) <= 122:
        output_string += chr(ord(char) - 32)
    else:
        output_string += char

#display the converted string
print('Reversed case text:', output_string)