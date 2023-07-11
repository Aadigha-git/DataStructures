# best algorithm if range is defined
# time complexity is heavily dependent on the range.

# non comparison algorithm
def counting_sort(lst):
    # Find the maximum element in the list
    max_value = max(lst)

    # Create a count list to store the frequency of each element
    count = [0] * (max_value + 1)

    # Count the occurrences of each element
    for num in lst:
        count[num] += 1

    # Calculate the cumulative sum of the count list
    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    # Create a new sorted list
    sorted_lst = [0] * len(lst)

    # Place elements in the sorted list based on the count and original order
    for num in lst:
        index = count[num] - 1
        sorted_lst[index] = num
        count[num] -= 1

    return sorted_lst


lst = [5, 4, 6, 7, 3, 9, 0]
sorted_lst = counting_sort(lst)
print(sorted_lst)
