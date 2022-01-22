
def find_subarrays(numbers, target):
    results = []
    for left in range(len(numbers)):
        product = 1
        for right in range(left, len(numbers)):
            if numbers[right] * product >= target:
                break
            product *= numbers[right]
            results.append(numbers[left:right+1])
    return results 

if __name__ == '__main__':
    print('should be [2], [5], [2, 5], [3], [5, 3], [10] -- ', find_subarrays([2, 5, 3, 10], target=30))
    print('should be [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] -- ', find_subarrays([8, 2, 6, 5], target=50))