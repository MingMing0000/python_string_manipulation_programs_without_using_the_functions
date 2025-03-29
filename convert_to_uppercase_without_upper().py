#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
#get string from user
#use ASCII value to convert lower case to upper case
#display the result

# get string from user
input_string = input("Enter a text to convert to uppercase: ")

# display user input
print("Original text:", input_string)

# convert to uppercase using ASCII values
output_string = ""
for char in input_string:
    # check if character is lowercase letter
    if ord(char) >= 97 and ord(char) <= 122:
        # convert to uppercase by subtracting 32 from ASCII value
        output_string += chr(ord(char) - 32)
    else:
        # keep the character if it's not lowercase
        output_string += char