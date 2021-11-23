
"""

[2, 5, 3, 10] t = 30

2
2 5 
2 5 3 !!
2 5 3 10 !!

5 
5 3
5 3 10 !! 

3
3 10 !!

10 


[2], [2, 5], [5], [5, 3], [3], [10]
"""

# O(N^2)
def find_subarrays(numbers, target):
    result = []
    for i in range(len(numbers)):
        product = 1
        for j in range(i, len(numbers)):
            product *= numbers[j]
            if product < target: 
                result.append(numbers[i:j+1])
    return result 


def num_subarrays(numbers, target):
    left = 0
    count = 0
    product = 1
    for right in range(len(numbers)):
        product *= numbers[i]
        while product >= target and left <= right:
            product /= numbers[left]
            left += 1
        count += right - left + 1
    return count


if __name__ == '__main__':
    print('should be [2], [5], [2, 5], [3], [5, 3], [10] -- ', find_subarrays([2, 5, 3, 10], target=30))
    print('should be [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] -- ', find_subarrays([8, 2, 6, 5], target=50))