#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
#have a string
#have a prefix
#remove the prefix from the string
#display the result

#sample string
string = "Hello"
#sample prefix
prefix = "Hell"

#test if prefix is in the string
if string[:len(prefix)] == prefix:
    #remove the prefix then print
    print(string[len(prefix):]) #output: o
else:
    #print the string
    print(string)