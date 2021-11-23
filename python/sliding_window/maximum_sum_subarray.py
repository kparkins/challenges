

def max_sub_array_of_size_k_(k, arr):
    if k <= 0: 
        return 0 
    if k >= len(arr):
        return sum(arr)
    max_sum = sum(arr[:k])
    start = 1
    for end in range(k+1, len(arr)+1):
        # this is bad because sum() makes this O(N*K)
        max_sum = max(max_sum, sum(arr[start:end]))
        start +=1 
    return max_sum

def max_sub_array_of_size_k(k, arr):
    if k <= 0:
        return 0
    if k >= len(arr):
        return sum(arr)
    curr_sum = 0
    max_sum = arr[0]
    window_start = 0
    for window_end in range(len(arr)):
        curr_sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[window_start]
            window_start += 1
    return max_sum

if __name__ == '__main__': 
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))