#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
#get string from user
#get what will be counted
#loop through each character then count
#display the result

#get string from user
input_string = input('Enter a text:')

#get what to find and count
what_to_count = input('What part of text you want to count how many times it appeared in the text?:')

#print(input_string.count(what_to_count))

#loop through the string and start counting
occurence_counter = 0
for i in range(0, len(input_string) - len(what_to_count) + 1):
    if input_string[i:i+len(what_to_count)] == what_to_count:
        occurence_counter += 1