#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#get input from user
#check if all characters are lower case using ASCII values
#display result

#get input from user
input_string = input("Enter a text to check if all letters are in lowercase: ")

#check if all characters are lower case using ASCII values
all_lowercase = True
for char in input_string:
    if not (ord('a') <= ord(char) <= ord('z')):
        all_lowercase = False
        break

#display the result
if all_lowercase == True:
    print("ALL letters in the text are in lowercase.")
else:
    print("NOT all letters in the text are in lowercase.")