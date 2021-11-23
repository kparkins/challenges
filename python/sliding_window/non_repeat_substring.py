from collections import defaultdict


def non_repeat_substring_loop(string):
    max_length = 0
    window_start = 0
    seen = defaultdict(int)
    for window_end in range(len(string)):
        seen[string[window_end]] += 1
        while seen[string[window_end]] > 1: 
            count = seen.pop(string[window_start])
            if count - 1 > 0: 
                seen[string[window_start]] = count - 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


'''def non_repeat_substring(string):
    seen = {} 
    max_length = 0
    window_start = 0
    for window_end in range(len(string)):
        char = string[window_end]
        if char in seen and window_start <= seen[char] <= window_end:
            window_start = seen[char] + 1
        seen[char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length'''

def non_repeat_substring(string):
    seen = {}
    max_length = 0
    window_start = 0
    for window_end in range(len(string)):
        char = string[window_end]
        if char in seen:
            window_start = seen[char] + 1
        seen[char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__': 
    print('should be 0', non_repeat_substring(""))
    print('should be 1', non_repeat_substring("A"))
    print('should be 2', non_repeat_substring('AB'))
    print('should be 3', non_repeat_substring('ABC'))
    print('should be 2', non_repeat_substring('AAC'))
    print('should be 2', non_repeat_substring('ACC'))
    print('should be 2', non_repeat_substring('DDAAC'))
    print('should be 3', non_repeat_substring('DDACC'))

    print('should be 3', non_repeat_substring('aabccbb'))
    print('should be 2', non_repeat_substring('abbbb'))
    print('should be 3', non_repeat_substring('abccde'))

