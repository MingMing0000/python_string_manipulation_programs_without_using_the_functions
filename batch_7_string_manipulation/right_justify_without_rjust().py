#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
#get the string from user   
#get the number of characters from user
#subtract the length of the string from the number of characters
#add space characters at the beginning times the result of the subtraction
#display the result

#get the string from user
input_string = input("Enter a text to justify:")

# get the number of characters from user
input_length = int(input("How many characters long you want the text to be?: "))

#display original text
print(f"Original text: '{input_string}'")