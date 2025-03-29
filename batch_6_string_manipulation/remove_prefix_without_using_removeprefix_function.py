#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
#have a string
#have a prefix
#remove the prefix from the string
#display the result

#sample string
string = input('Enter some text: ')
#sample prefix
prefix = input('Enter the prefix you want to remove: ')

#display the user's input
print("Original text:", string)
print("Prefix to remove:", prefix)

#test if prefix is in the string
if string[:len(prefix)] == prefix:
    #remove the prefix then print
    print(f'output: {string[len(prefix):]}')
else:
    #print the string
    print(f'output: {string}')