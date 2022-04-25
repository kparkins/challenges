import math


def find_first_index_of_k(array, k):
    left = 0
    result = -1
    right = len(array) - 1
    while left <= right:
        mid = ((right - left) // 2) + left
        if array[mid] == k:
            result = mid
            right = mid - 1
        elif array[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return result


def test_find_first_index_of_k():
    array = [1, 2, 3, 4, 4, 5, 6]
    assert 3 == find_first_index_of_k(array, 4)

    array = [1, 2, 3, 4, 4, 5, 6]
    assert 0 == find_first_index_of_k(array, 1)

    array = [1, 2, 3, 4, 4, 5, 6]
    assert 6 == find_first_index_of_k(array, 6)

    array = [4, 4, 4, 4, 4, 4]
    assert 0 == find_first_index_of_k(array, 4)


def integer_square_root(k):
    left = 1
    right = k
    while left <= right:
        mid = ((right - left) // 2) + left
        mid_square = mid * mid
        if mid_square == k or (mid_square < k and (mid+1) ** 2 > k):
            return mid
        elif mid_square < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def test_integer_square_root():
    assert 15 == integer_square_root(225)
    assert 10 == integer_square_root(100)
    assert 4 == integer_square_root(16)
    assert 2 == integer_square_root(4)
    assert 1 == integer_square_root(1)
    assert int(math.isqrt(5)) == integer_square_root(5)
    for i in range(1, 1000):
        assert int(math.isqrt(i)) == integer_square_root(i)
