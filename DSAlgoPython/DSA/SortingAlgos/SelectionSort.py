def selection_sort(lst):
    indexing_length = range(0, len(lst)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_value]:
                min_value = j


        if min_value != i:
            lst[min_value], lst[i] = lst[i], lst[min_value]

    return lst

lst = [5,4,6,7,3,9,0]
print(selection_sort(lst))