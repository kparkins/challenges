
def dutch_flag_sort(numbers):
    cursor = 0
    low, high = 0, len(numbers) - 1
    while cursor <= high:
        if numbers[cursor] == 2:
            numbers[cursor], numbers[high] = numbers[high], numbers[cursor]
            high -= 1
        elif numbers[cursor] == 0:
            numbers[cursor], numbers[low] = numbers[low], numbers[cursor]
            low += 1
            cursor += 1
        else:
            cursor += 1
    return numbers
    


if __name__ == '__main__':
    print('should be [0, 0, 1, 1, 2]', dutch_flag_sort([1,0,2,1,0]))
    print('should be [0, 0, 1, 2, 2, 2]', dutch_flag_sort([2, 2, 0, 1, 2, 0]))
