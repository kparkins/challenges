import math
from collections import Counter


def triplet_sum_to_zero(numbers):
    results = set()
    numbers.sort()
    frequencies = Counter(n for n in numbers)
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            v1 = numbers[i]
            v2 = numbers[j]
            v3 = -(v1 + v2)
            if v3 not in frequencies:
                continue
            count = frequencies[v3]
            if v1 == v3:
                count -= 1
            if v2 == v3:
                count -= 1
            if count > 0:
                results.add(tuple(sorted([v1, v2, v3])))
    return [list(x) for x in results]


def triplet_sum_to_zero_two_pointers(numbers):
    triplets = []
    numbers.sort()
    for cursor in range(len(numbers) - 2):
        if cursor > 0 and numbers[cursor] == numbers[cursor-1]:
            continue
        i = cursor + 1
        j = len(numbers) - 1
        while i < j:
            current_sum = numbers[cursor] + numbers[i] + numbers[j]
            if current_sum == 0:
                triplets.append([numbers[cursor], numbers[i], numbers[j]])
                i += 1
                j -= 1
                while i < j and numbers[i] == numbers[i-1]:
                    i += 1
                while i < j and numbers[j] == numbers[j+1]:
                    j -= 1
            if current_sum < 0:
                i += 1
            elif current_sum > 0:
                j -= 1
    return triplets


def triplet_sum_close_to_target(numbers, target):
    numbers.sort()
    closest_sum = math.inf
    for cursor in range(len(numbers) - 2):
        left, right = cursor + 1, len(numbers) - 1
        while left < right:
            current_sum = numbers[cursor] + numbers[left] + numbers[right]
            difference = abs(target - current_sum) 
            if abs(target - closest_sum) == difference:
                closest_sum = min(closest_sum, current_sum)
            elif abs(target - closest_sum) >  difference:
                closest_sum = current_sum
            if current_sum == target:
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum
            


def triplet_with_smaller_sum(numbers, target):
    count = 0
    numbers.sort()
    for cursor in range(len(numbers) - 2):
        left = cursor + 1
        right = len(numbers) - 1
        while left < right:
            if numbers[cursor] + numbers[left] + numbers[right] < target:
                count += right - left
                left += 1
            else: 
                right -= 1
    return count


if __name__ == '__main__':
    print('should be [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1] --',
          triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))
    print('should be [[-5, 2, 3], [-2, -1, 3]] --',
          triplet_sum_to_zero([-5, 2, -1, -2, 3]))

    print('should be [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1] --',
          triplet_sum_to_zero_two_pointers([-3, 0, 1, 2, -1, 1, -2]))
    print('should be [[-5, 2, 3], [-2, -1, 3]] --',
          triplet_sum_to_zero_two_pointers([-5, 2, -1, -2, 3]))

    print('should be 1', triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print('should be 0', triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print('should be 3', triplet_sum_close_to_target([1, 0, 1, 1], 100))

    print('should be 2', triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print('should be 4', triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
