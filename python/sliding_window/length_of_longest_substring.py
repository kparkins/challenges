from collections import Counter, defaultdict

def _edit_distance(counter):
    most_common = counter.most_common()
    if len(most_common) <= 0:
        return 0
    return sum(v for k, v in counter.items() if k != most_common[0][0])

def length_of_longest_substring_inefficient(string, k):
    max_length = 0
    window_start = 0
    counts = Counter()
    for window_end in range(len(string)):
        counts[string[window_end]] += 1 
        while _edit_distance(counts) > k: 
            char = string[window_start]
            counts[char] -= 1
            if counts[char] <= 0:
                counts.pop(char)
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# |a a a b b c|

'''def length_of_longest_substring(string, k):
    max_length = 0
    window_start = 0
    frequencies = {}
    most_frequent_count = 0
    for window_end in range(len(string)):
        last_character = string[window_end]
        if last_character not in frequencies:
            frequencies[last_character] = 0
        frequencies[last_character] += 1
        most_frequent_count = max(most_frequent_count, frequencies[last_character])
        if window_end - window_start + 1 - most_frequent_count > k:
            frequencies[string[window_start]] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
'''

def length_of_longest_substring(string, k):
    max_length = 0
    window_start = 0
    seen = defaultdict(int)
    most_occurences = 0
    for window_end in range(len(string)):
        seen[string[window_end]] += 1
        most_occurences = max(most_occurences, seen[string[window_end]])
        while window_end - window_start + 1 - most_occurences > k:
            seen[string[window_start]] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length 

'''def length_of_longest_substring_ones(string, k):
    ones_count = 0
    max_length = 0
    window_start = 0
    for window_end in range(len(string)):
        ones_count += string[window_end]
        while window_end - window_start + 1 - ones_count > k:
            ones_count -= string[window_start]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length'''

def length_of_longest_substring_ones(string, k):
    ones_count = 0
    window_start = 0
    max_length = 0
    for window_end in range(len(string)):
        if string[window_end] == 1:
            ones_count += 1
        while window_end - window_start + 1 - ones_count > k:
            if string[window_start] == 1:
                ones_count -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

if __name__ == '__main__':
    print('should be 5', length_of_longest_substring('aabccbb', 2))
    print('should be 4', length_of_longest_substring('abbcb', 1))
    print('should be 3', length_of_longest_substring('abccde', 1))
    print('should be 5', length_of_longest_substring('aaabbc', 2))

    print('should be 6', length_of_longest_substring_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print('should be 9', length_of_longest_substring_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

