# basic datatypes
#integer    int 123
#string     'str' "str" "hello" '23'
#boolean    True False 
#float      float 3.22

#declaring variables
name = 'Aadi'
print(name)

name = 'bob'
print(name)

age = 18
print(age)

# variable limitations 
# can contain underscores, text
# cannot contain dashes,  start with a number

## lists 
# collection of different datatypes
# items separated by a comma
fruits = ['apple', 'pear']
print(fruits[1])
fruits.append('strawberry')
print(fruits)
# Changing/ Replacing item
fruits[1] = 'blueberry'
print(fruits)


#tuple
# used for coordinates generally
color = (255,255,255)
print(type(color))
position = (2,3)