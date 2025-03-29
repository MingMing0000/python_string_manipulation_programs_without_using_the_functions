#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#get string from user
#loop through the string
#locate the position from right

#get string from user
input_string = input("Enter a text:")
index_parameter = input("Enter the text you want to find and locate in the text:")

#print(input_string.rindex(index_parameter))

#loop through the string then display the position
for i in range(len(input_string) - len(index_parameter), -1, -1):
    if input_string[i:i+len(index_parameter)] == index_parameter:
        print(f'The first appearance of "{index_parameter}" starting from the right at position {i}')
        break
else:
    print(f'"{index_parameter}" was not found in the text.')