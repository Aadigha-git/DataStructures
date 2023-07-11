pos = -1 # Global Variable

def search(list, n):
    """ using enumerate
    for i, num in enumerate(list):
        if num == n:
            return i
    return -1
    """ 

    # using for loop
    global pos
    for i in range(len(list)):
        if list[i] == n:
            pos += 1
            globals()['pos'] = i + 1
            return True
    return False
    

    """  using while loop
    while i<len(list):
        if list[i]==n:
            # local Variable pos = i 
            globals()['pos'] = i+1
            return True
        i = i+1 
    """

list = [5,4,6,7,3,9,0]
n = int(input("Enter the number you want to search for: "))

if search(list, n):
    print("Found at position", pos)
else:
    print("Not found.")