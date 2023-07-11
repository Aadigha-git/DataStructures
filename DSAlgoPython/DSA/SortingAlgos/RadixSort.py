# non comparison algorithm
def radix_sort(lst):
    # Find the maximum element to determine the number of digits
    max_value = max(lst)
    num_digits = len(str(max_value))

    # Perform counting sort for each digit from least significant to most significant
    for digit_index in range(num_digits):
        lst = counting_sort_by_digit(lst, digit_index)

    return lst


def counting_sort_by_digit(lst, digit_index):
    count = [0] * 10  # Counting array for digits 0-9
    output = [0] * len(lst)  # Output array to store sorted elements

    # Count the occurrences of each digit
    for num in lst:
        digit = (num // (10 ** digit_index)) % 10
        count[digit] += 1

    # Calculate the cumulative sum of the count list
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place elements in the output array based on the digit and original order
    for i in range(len(lst) - 1, -1, -1):
        num = lst[i]
        digit = (num // (10 ** digit_index)) % 10
        output[count[digit] - 1] = num
        count[digit] -= 1

    return output


lst = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_lst = radix_sort(lst)
print(sorted_lst)
