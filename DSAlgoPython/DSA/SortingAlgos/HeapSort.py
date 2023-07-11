def heap_sort(lst):
    n = len(lst)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # Swap the root (maximum value) with the last element
        heapify(lst, i, 0)  # Heapify the reduced heap

    return lst


def heapify(lst, n, root):
    largest = root  # Initialize the largest element as the root
    left = 2 * root + 1
    right = 2 * root + 2

    # Check if the left child of the root exists and is larger than the root
    if left < n and lst[left] > lst[largest]:
        largest = left

    # Check if the right child of the root exists and is larger than the current largest
    if right < n and lst[right] > lst[largest]:
        largest = right

    # If the largest element is not the root, swap them and recursively heapify the affected sub-tree
    if largest != root:
        lst[root], lst[largest] = lst[largest], lst[root]
        heapify(lst, n, largest)


lst = [5, 4, 6, 7, 3, 9, 0]
sorted_lst = heap_sort(lst)
print(sorted_lst)
