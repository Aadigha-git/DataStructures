# optimised implementation
def binary_search(lst, target):
    lb = 0                  # lower bound
    ub = len(lst) - 1       # upper bound

    while lb <= ub:
        mid = (lb + ub) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lb = mid + 1
        else:
            ub = mid - 1

    return -1


numbers = [4, 7, 8, 12, 36, 45, 99]
n = int(input("Enter the number you want to search for: "))

index = binary_search(numbers, n)
if index != -1:
    print(f"Found at position {index}")
else:
    print("Not found.")

"""
pos = -1

def search(lst,n):
    lst.sort()
    lB = 0 # lower boud
    uB = len(lst) - 1 # upper bound
    
    while lB <= uB:
        mid = (lB+uB) // 2
        if lst[mid] == n:
            globals()['pos'] = mid+1
            return True
        elif lst[mid] < n:        
                lB= mid + 1
        else:
                uB = mid - 1
    return False

lst = [4, 7, 8, 12, 45, 99]
n = int(input("Enter the number you want to search for: "))

if search(lst,n):
    print("Found at ",pos)
else:
    print("Not Found")
"""
print()
"""
When I was searching for the number 36 in the list 
lst = [4, 7, 8, 12, 45, 99, 36]
I was unable to find 36 because the list is not in sorted order. 
For binary search to execute properly, The list needs to be sorted
"""