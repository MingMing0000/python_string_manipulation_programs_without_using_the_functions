#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#get input from user
#check if the string start with the given string
#display the result

#get input from user
input_string = input("Enter a text: ")
start_string = input("Enter the part to be used to check if the text starts with that part: ")

print(f'does the text "{input_string}" start with "{start_string}"?')

#check if the string start with the given string
if input_string[:len(start_string)] == start_string:
    print(f"Yes, the text '{input_string}' starts with '{start_string}'")
else:
    print(f"No, the text '{input_string}' does not start with '{start_string}'")