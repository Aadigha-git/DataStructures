def bucket_sort(lst):
    min_value = min(lst)
    max_value = max(lst)
    bucket_size = 10  # Set the bucket size

    # Determine the range and size of each bucket
    bucket_range = (max_value - min_value + 1) / bucket_size
    buckets = [[] for _ in range(bucket_size)]

    # Assign elements to the appropriate bucket
    for num in lst:
        index = int((num - min_value) / bucket_range)
        buckets[index].append(num)

    # Sort elements within each bucket using another sorting algorithm (e.g., insertion sort)
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate the sorted buckets into a single list
    sorted_lst = [num for bucket in buckets for num in bucket]

    return sorted_lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


lst = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_lst = bucket_sort(lst)
print(sorted_lst)
