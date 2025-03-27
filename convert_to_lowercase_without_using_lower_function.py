#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
#have a string in upper case
#create a dictionary with key as upper case and value as lower case
#change the string to lower case using dictionary
#Print the string

#have a string in upper case
string = input('Enter a text to convert to lower case: ')
print("Original text:", string)

#create a dictionary with key as upper case and value as lower case
upper_to_lower = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}

#change the string to lower case using dictionary
lower_string = ""
for char in string:
    if char not in upper_to_lower:
        lower_string += char
    else:
        lower_string += upper_to_lower[char]

#Print the string
print('Converted text:', lower_string)