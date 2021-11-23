from collections import defaultdict

# this is max length sub-array with at most K distinct items
'''def fruits_into_baskets(fruits):
    max_fruits = 0    
    window_start = 0
    baskets = defaultdict(int)
    for window_end in range(len(fruits)):
        baskets[fruits[window_end]] += 1
        while len(baskets) > 2:
            count = baskets.pop(fruits[window_start])
            if count - 1 > 0: 
                baskets[fruits[window_start]] = count - 1
            window_start += 1
        max_fruits = max(max_fruits, window_end - window_start + 1)      
    return max_fruits'''

def fruits_into_baskets(fruits):
    max_fruits = 0
    window_start = 0
    baskets = defaultdict(int)
    for window_end in range(len(fruits)):
        baskets[fruits[window_end]] += 1
        while len(baskets) > 2:
            num_fruits = baskets.pop(fruits[window_start])
            if num_fruits - 1 > 0:
                baskets[fruits[window_start]] = num_fruits - 1
            window_start += 1
        max_fruits = max(max_fruits, window_end - window_start + 1)
    return max_fruits

if __name__ == '__main__':
    print("should be 3: ", fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print("should be 5: ", fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
    print("should be 4: ", fruits_into_baskets(['Z', 'C', 'Z', 'Z', 'K']))
    print("should be 5: ", fruits_into_baskets(['Z', 'Z', 'Z', 'Z', 'Z']))
    print("should be 2: ", fruits_into_baskets(['Z', 'X', 'C', 'D', 'K']))
    print("should be 2: ", fruits_into_baskets([ 'C', 'D', 'K','Z', 'X']))
    print("should be 1: ", fruits_into_baskets(['C']))
    print("should be 0: ", fruits_into_baskets([]))

