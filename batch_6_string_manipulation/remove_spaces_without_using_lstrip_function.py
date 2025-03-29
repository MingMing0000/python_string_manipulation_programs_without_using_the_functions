#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
#create a string
#remove the space characters at the beginning of the string
#display the result

#display the program title
print('Leading space remover')

# create a string
string = input('Enter a text(put some spaces before the first word to see how the program functions): ')
print("Original text:", string)

# remove the space characters at the beginning of the string
output = ""
non_space = False

for char in string:
    if not non_space and char != " ":
        non_space = True
    if non_space:
        output += char

# display the result
print(f'Text with spaces removed:{output}')