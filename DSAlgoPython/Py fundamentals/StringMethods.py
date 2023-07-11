##.strip()
# removes all leading and trailing whitespaces from a string
text = input('Input something!')
textn = text.strip()
print(type(text))
# do not directly define a variable to a print statement
# you will return with a null type, which is invalid
print(type(textn))

#.lower()
# makes everything into lower case

#.upper()
#makes everything into upper case

#.split()
# makes a list of the characters in the string
print(textn.split(' '))

#This is a function
# len()
# returns the length of the string or list
print(len(text))
print(len(textn))

