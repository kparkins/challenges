
def remove_duplicates_(nums):
    cursor = 0
    for runner in range(len(nums)):
        if nums[cursor] != nums[runner]:
            cursor += 1
            nums[cursor] = nums[runner]
    return cursor+1


def remove_element(nums, key):
    cursor = 0
    for runner in range(len(nums)):
        if nums[runner] != key:
            nums[cursor] = nums[runner]
            cursor += 1
    return cursor


def remove_duplicates(nums):
    cursor = 0
    for runner in range(1, len(nums)):
        if nums[runner] != nums[runner - 1]:
            cursor += 1
            nums[cursor] = nums[runner]
    return cursor+1


if __name__ == '__main__':
    print('should be 4', remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print('should be 2', remove_duplicates([2, 2, 2, 11]))

    print('should be 4', remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print('should be 2', remove_element([2, 11, 2, 2, 1], 2))
