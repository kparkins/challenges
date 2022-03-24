
def search_quadruplets(numbers, target):
    if len(numbers) < 4:
        return []
    results = []
    numbers.sort()
    for i in range(len(numbers) - 3):
        for j in range(i+1, len(numbers) - 2):
            left = j+1
            right = len(numbers) - 1
            while left < right:
                current_sum = numbers[i] + numbers[j] + \
                    numbers[left] + numbers[right]
                if current_sum == target:
                    results.append(
                        [numbers[i], numbers[j], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left-1]:
                        left += 1
                    while right > left and numbers[right] == numbers[right+1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
    return results


if __name__ == '__main__':
    print('Should be [-3, -1, 1, 4], [-3, 1, 1, 2] -- ',
          search_quadruplets([4, 1, 2, -1, 1, -3], target=1))
    print('Should be [-2, 0, 2, 2], [-1, 0, 1, 2] -- ',
          search_quadruplets([2, 0, -1, 1, -2, 2], target=2))
