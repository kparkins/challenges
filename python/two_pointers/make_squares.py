
def make_squares(nums):
    cursor = len(nums) - 1 
    squares = [0] * len(nums)
    left, right = 0, len(nums) - 1
    while left < right: 
        left_square = nums[left]**2
        right_square = nums[right]**2
        if right_square > left_square:
            squares[cursor] = right_square
            right -= 1
        else: 
            squares[cursor] = left_square
            left += 1
        cursor -= 1
    return squares

if __name__ == '__main__':
    print('should be [0, 1, 4, 4, 9]', make_squares([-2, -1, 0, 2, 3]))
    print('should be [0, 1, 1, 4, 9]', make_squares([-3, -1, 0, 1, 2]))
