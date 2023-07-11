text = input('Username: ')
try:
    number = int(text)
    print('Valid Username!')
except:
    print('invalid username')