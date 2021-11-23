
'''def pair_with_targetsum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1 
        elif current > target:
            right -= 1
    return [-1, -1]'''

def pair_with_targetsum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

if __name__ == '__main__':
    print('should be [1, 3]', pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print('should be [0, 2]', pair_with_targetsum([2, 5, 9, 11], 11))