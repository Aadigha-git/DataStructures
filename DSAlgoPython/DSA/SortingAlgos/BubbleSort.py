def bubble_sort(lst):
    indexing_length = len(lst)-1    # because you cant make comparisons with the last element and last + 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if lst[i] > lst[i+1]:
                sorted = False
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
            

lst = [5,4,6,7,3,9,0]
print(bubble_sort(lst))