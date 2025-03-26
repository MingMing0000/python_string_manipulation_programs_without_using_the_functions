#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
#have a string
#create algorithm to check if the string end part is same
#print the result

#create a string
string = "Hello Kitty"
print('Word:', string)

#set the end part to check
end_part = "ty"
print(f'Does it end with "{end_part}"?')

#check if the string end part is same
if string[-len(end_part):] == end_part:
    print(f"Yes, the word {string} ends with {end_part}")
else:
    print(f"No, the word {string} does not end with {end_part}")