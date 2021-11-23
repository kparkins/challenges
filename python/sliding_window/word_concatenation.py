from collections import Counter

def find_word_concatenation(string, words):
    indices = []
    word_size = len(words[0])
    window_size = word_size * len(words)
    frequencies = Counter(w for w in words)
    for window_end in range(window_size, len(string)+1):
        seen = Counter()
        for window_start in range(window_end-window_size, window_end, word_size): 
            word = string[window_start:window_start+word_size]
            if word in frequencies: 
                seen[word] += 1
            else:
                break
        if len(frequencies-seen) == 0:
            indices.append(window_end-window_size)
    return indices

if __name__ == '__main__':
    print('should be [0, 3]', find_word_concatenation('catfoxcat', ['cat', 'fox']))
    print('should be [3]', find_word_concatenation('catcatfoxfox', ['cat', 'fox']))