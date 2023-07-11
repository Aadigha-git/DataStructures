fruits = ['apple', 'pear']
print(fruits[1])
fruits.append('strawberry')
print(fruits)

#priniting every element by iteration through a list
for fruit in fruits:
    print(fruit)

#otherwise printing by index iteration
for x in range(len(fruits)):
    if fruits[x]=='pear':
        print(fruits[x])
    else:
        print('Not a pear :(') 