from bisect import bisect_left

def make_squares(arr):
    result = []
    i = bisect_left(arr, 0)
    j = i - 1
    for _ in range(len(arr)):
        if j >= 0 and i < len(arr):
            if abs(arr[i]) < abs(arr[j]):
                result.append(arr[i] * arr[i])
                i += 1
            else:
                result.append(arr[j] * arr[j])
                j -= 1
        elif j >= 0:
            result.append(arr[j] * arr[j])
            j -= 1
        elif i < len(arr):
            result.append(arr[i] * arr[i])
            i += 1
    return result

if __name__ == '__main__':
    print('should be [0, 1, 4, 4, 9]', make_squares([-2, -1, 0, 2, 3]))
    print('should be [0, 1, 1, 4, 9]', make_squares([-3, -1, 0, 1, 2]))
