#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
#create a string
#remove the space characters at the beginning of the string
#display the result

#display the program title
print('Leading space remover')

# create a string
string = input('Enter a text: ')
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
print(f'output: {output}')