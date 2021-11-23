import math
from collections import Counter

def triplet_sum_to_zero(numbers):
    results = set()
    targets = Counter(numbers)
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            diff = -(numbers[i] + numbers[j])
            if diff not in targets:
                continue
            count = targets[diff] 
            if numbers[i] == diff:
                count -= 1 
            if numbers[j] == diff:
                count -= 1
            if count > 0:
                results.add(tuple(sorted([numbers[i], numbers[j], diff])))
    return [list(x) for x in results]


def triplet_sum_to_zero_two_pointers(numbers):
    triplets = []
    numbers.sort()
    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i-1]:
            continue
        left = i + 1
        right = len(numbers) - 1
        while left < right: 
            triplet = numbers[i] + numbers[left] + numbers[right]
            if triplet == 0:
                triplets.append([numbers[i], numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1 
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif triplet < 0:
                left += 1
            else: 
                right -= 1
    return triplets


def triplet_sum_close_to_target(numbers, target):
    numbers.sort()
    closest_sum = 0
    closest_distance = math.inf
    for i in range(len(numbers)-2):
        left = i + 1
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            current_distance = current_sum - target
            if abs(current_distance) < abs(closest_distance) or \
                (abs(current_distance) == abs(closest_distance) and current_sum < closest_sum):
                closest_sum = current_sum
                closest_distance = current_distance
            if current_distance < 0:
                left += 1
            else:
                right -= 1
    return closest_sum


def triplet_with_smaller_sum(numbers, target):
    numbers.sort()
    num_triplets = 0
    for i in range(len(numbers) - 2):
        left = i + 1
        right = len(numbers) - 1
        while left < right: 
            current_sum = numbers[i] + numbers[left] + numbers[right]
            if current_sum < target:
                num_triplets += right - left
                left += 1
            elif current_sum >= target:
                right -= 1
    return num_triplets 


if __name__ == '__main__':
    print('should be [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1] --', triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))
    print('should be [[-5, 2, 3], [-2, -1, 3]] --', triplet_sum_to_zero([-5, 2, -1, -2, 3]))

    print('should be [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1] --', triplet_sum_to_zero_two_pointers([-3, 0, 1, 2, -1, 1, -2]))
    print('should be [[-5, 2, 3], [-2, -1, 3]] --', triplet_sum_to_zero_two_pointers([-5, 2, -1, -2, 3]))

    print('should be 1', triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print('should be 0', triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print('should be 3', triplet_sum_close_to_target([1, 0, 1, 1], 100))

    print('should be 2', triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print('should be 4', triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))