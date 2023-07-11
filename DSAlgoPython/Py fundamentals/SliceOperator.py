#can be used on strings and lists
#[start:stop:step]

fruits = ['apples', 'pears', 'figs', 'kiwis']
text = 'What why where when how'

print(fruits[0:len(fruits):2])
print(text[0:len(text):2])

# for adding
fruits[1:1] = 'b'
print(fruits)