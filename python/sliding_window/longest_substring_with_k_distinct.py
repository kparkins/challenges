from collections import defaultdict

'''def longest_substring_with_k_distinct(string, k):
  max_length = 0 
  window_start = 0
  seen = defaultdict(int)
  for window_end in range(len(string)):
    seen[string[window_end]] += 1
    while len(seen) > k:
      count = seen.pop(string[window_start])
      count -= 1
      if count > 0:
        seen[string[window_start]] = count
      window_start += 1   
    max_length = max(max_length, window_end - window_start + 1)
  return max_length'''

def longest_substring_with_k_distinct(string, k):
  longest = 0
  window_start = 0
  seen = defaultdict(int)
  for window_end in range(len(string)):
    seen[string[window_end]] += 1
    while len(seen) > k:
      count = seen.pop(string[window_start])
      if count > 1:
        seen[string[window_start]] = count - 1
      window_start += 1
    longest = max(longest, window_end - window_start + 1)
  return longest

if __name__ == '__main__':
  print(longest_substring_with_k_distinct('araaci', 2))
  print(longest_substring_with_k_distinct('araaci', 1))
  print(longest_substring_with_k_distinct('cbbebi', 3))
  print(longest_substring_with_k_distinct('cbbebi', 10))