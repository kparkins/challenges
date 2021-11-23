from collections import Counter


def find_string_anagrams(string, pattern):
    matches = 0
    indices = []
    window_start = 0
    seen = Counter(p for p in pattern)
    for window_end in range(len(string)):
        end_character = string[window_end]
        if end_character in seen:
            seen[end_character] -= 1
            if seen[end_character] == 0:
                matches += 1
        if matches == len(seen):
            indices.append(window_start)
        if window_end - window_start + 1 >= len(pattern):
            start_character = string[window_start]
            if seen[start_character] == 0:
                matches -= 1
            seen[start_character] += 1
            window_start += 1
    return indices


def find_string_anagrams_(string, pattern):
    matches = 0
    indices = []
    window_start = 0
    frequencies = Counter(p for p in pattern)
    for window_end in range(len(string)):
        end_char = string[window_end]
        if end_char in frequencies:
            frequencies.subtract(end_char)
            if frequencies[end_char] == 0:
                matches += 1
        if window_end - window_start + 1 > len(pattern):
            start_char = string[window_start]
            if start_char in frequencies:
                if frequencies[start_char] == 0:
                    matches -= 1
                frequencies.update(start_char)
            window_start += 1
        if matches == len(frequencies):
            indices.append(window_start)
    return indices


if __name__ == '__main__':
    print('should be [1, 2]', find_string_anagrams('ppqp', 'pq'))
    print('should be [2, 3, 4]', find_string_anagrams('abbcabc', 'abc'))
