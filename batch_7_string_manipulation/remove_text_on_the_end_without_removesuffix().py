#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
#get the string from user 
#remove the suffix by using len() then compare the string with the suffix
#display the result

#get the string from user
input_string = input('Enter some text: ')

#get the suffix from user
suffix = input('Enter the suffix you want to remove: ')

#display the user's input
print("Original text:", input_string)
print("Suffix to remove:", suffix)

#test if suffix is in the string
if input_string[-len(suffix):] == suffix:
    #remove the suffix then print
    print(f'\nText with suffix removed: {input_string[:-len(suffix)]}')
else:
    #print the string
    print(f'\nsuffix don\'t match, output text will be the same: {input_string}')