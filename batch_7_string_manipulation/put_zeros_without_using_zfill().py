#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
#get string from user
#subtract character count to the length of string
#multiply result of subtract to the string '0'
#display the result

#get input from user
input_string = input('Enter some text or numbers:')
zero_input = int(input('How many characters long you want the text to be?:'))

#subtract the length of string to character count input
output_string = zero_input - len(input_string)

#print(input_string.zfill(zero_input))
#add the zeros then display the result
print(f'Text with zeros in the beginning:{'0' * output_string}{input_string}')