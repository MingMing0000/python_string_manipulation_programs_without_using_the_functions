#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
#get the string from user
#remove the spaces by splitting the string and joining it again
#display the result

print("This program removes the spaces at the end of the text")
#get the string from user
input_string = input("Enter a text(put as many spaces as you like after the text):")

#display the original string
print(f"Original text:{input_string}")

#remove the spaces by splitting the string and joining it again
words = input_string.split()
output_string = " ".join(words)