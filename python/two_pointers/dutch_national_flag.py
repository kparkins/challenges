
def dutch_flag_sort_single_pass(numbers):
    left = 0
    cursor = 0
    right = len(numbers) - 1
    while cursor <= right:
        if numbers[cursor] == 2:
            numbers[right], numbers[cursor] = numbers[cursor], numbers[right]
            right -= 1
        elif numbers[cursor] == 0:
            numbers[left], numbers[cursor] = numbers[cursor], numbers[left]
            cursor += 1
            left += 1
        else:
            cursor += 1
    return numbers


def dutch_flag_sort(numbers):
    cursor = 0
    right = len(numbers) - 1
    while cursor < right:
        if numbers[cursor] == 2:
            numbers[right], numbers[cursor] = numbers[cursor], numbers[right]
            right -= 1
        else:
            cursor += 1
    left = 0
    cursor = 0
    while cursor <= right:
        if numbers[cursor] == 0:
            numbers[left], numbers[cursor] = numbers[cursor], numbers[left]
            left += 1
        cursor += 1
    return numbers


if __name__ == '__main__':
    print('should be [0, 0, 1, 1, 2]', dutch_flag_sort([1,0,2,1,0]))
    print('should be [0, 0, 1, 2, 2, 2]', dutch_flag_sort([2, 2, 0, 1, 2, 0]))
