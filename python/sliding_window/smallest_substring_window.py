from collections import Counter

def find_substring(string, pattern):
    matches = 0
    window_start = 0
    smallest_window = ' ' * (len(string) + 1)
    frequencies = Counter(p for p in pattern)
    for window_end in range(len(string)):
        end_char = string[window_end]
        if end_char in frequencies: 
            frequencies.subtract(end_char)
            if frequencies[end_char] == 0:
                matches += 1
        while matches >= len(pattern):
            if window_end - window_start + 1 < len(smallest_window):
                smallest_window = string[window_start:window_end + 1]
            start_char = string[window_start]
            if start_char in frequencies: 
                if frequencies[start_char] == 0:
                    matches -= 1
                frequencies.update(start_char)
            window_start += 1
    return smallest_window.strip()


if __name__ == '__main__':
    print('should be \'abdec\'', find_substring('abdec', 'abc'))
    print('should be \'bca\'', find_substring('abdbca', 'abc'))
    print('should be \'\'', find_substring('adcad', 'abc'))