from collections import Counter, defaultdict

def find_permutation(string, pattern):
  matches = 0
  window_start = 0
  seen = Counter(p for p in pattern) 
  for window_end in range(len(string)):
    end_character = string[window_end]
    if end_character not in seen or seen[end_character] <= 0:
      while window_start < window_end:
        start_character = string[window_start]
        if start_character in seen:
          seen[start_character] += 1
          matches -= 1
        window_start += 1
    if end_character in seen and seen[end_character] > 0:
      matches += 1
      seen[end_character] -= 1
    while window_end - window_start + 1 > len(pattern):
      start_character = string[window_start]
      if start_character in seen:
        seen[start_character] += 1
        matches -= 1
      window_start += 1
    if matches == len(pattern):
      return True
  return False

def find_permutation_original(string, pattern):
    window_start = 0
    window_chars = Counter()
    pattern_chars = Counter(p for p in pattern)
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in pattern_chars:
            window_chars = Counter()
            window_start = window_end
        else:
            window_chars.update(right_char)
            if len(pattern_chars - window_chars) == 0:
                return True
    return False

def find_permutation_(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False
                

if __name__ == '__main__':
    print('should be True', find_permutation('bcaf', 'abc'))
    print('should be True', find_permutation('oidbcaf', 'abc'))
    print('should be False', find_permutation('odicf', 'dc'))
    print('should be True', find_permutation('bcdxabcdy', 'bcdyabcdx'))
    print('should be True', find_permutation('aacb', 'abc'))
