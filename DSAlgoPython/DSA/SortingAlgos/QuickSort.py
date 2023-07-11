def quick_sort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    items_greater = []
    items_lower = []

    for item in lst:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

lst = [5,4,6,7,3,9,0]
print(quick_sort(lst))