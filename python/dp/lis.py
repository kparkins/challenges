

def find_lis(array):
    dp = [1] * len(array)
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def test_find_lis():
    assert 3 == find_lis([1, 4, 3, 2, 3])

def find_lds(array):
    dp = [1] * len(array)
    for i in range(len(array)):
        for j in range(i):
            if array[j] > array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def test_find_lds():
    assert 3 == find_lds([1, 4, 3, 2, 3])
    assert 2 == find_lds([2,1])
    assert 1 == find_lds([1])
    assert 4 == find_lds([5, 4, 3, 2, 3])