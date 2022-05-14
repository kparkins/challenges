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


def index_of_min_cyclically_sorted(array):
    def get_neighbors(array, index):
        left = index - 1 if index - 1 >= 0 else len(array) - 1
        right = (index + 1) % len(array)
        return left, right

    if array is None or len(array) <= 0:
        return -1
    if len(array) == 1:
        return 0
    left = 0
    right = len(array)
    while left <= right:
        mid = ((right - left) // 2) + left
        li, ri = get_neighbors(array, mid)
        if array[li] > array[mid] and array[mid] < array[ri]:
            return mid
        elif array[li] < array[mid] and array[mid] > array[ri]:
            return ri
        elif array[li] < array[mid] < array[ri]:
            right = li
        elif array[li] > array[mid] > array[ri]:
            left = ri
    return -1


def test_index_of_min_cyclically_sorted():
    array = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    assert 4 == index_of_min_cyclically_sorted(array)

    array = [1, 2, 3, 4]
    assert 0 == index_of_min_cyclically_sorted(array)

    array = [4, 1, 2, 3]
    assert 1 == index_of_min_cyclically_sorted(array)


'''
# this does not produce a stable sort so the returned index may not
# point to the pivot value thus making our quickselect search incorrect

def partition(array, pivot, left, right):
    while left < right:
        while left < right and array[left] < pivot:
            left += 1
        while left < right and array[right] > pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
    return right'''


def partition(array, pivot_index, left, right):
    store_index = left
    pivot_value = array[pivot_index]
    array[right], array[pivot_index] = array[pivot_index], array[right]
    for j in range(left, right):
        if array[j] < pivot_value:
            array[store_index], array[j] = array[j], array[store_index]
            store_index += 1
    array[store_index], array[right] = array[right], array[store_index]
    return store_index


def __find_kth_largest(array, left, right, kindex):
    pivot_index = partition(array, kindex, left, right)
    if pivot_index < kindex:
        return _find_kth_largest(array, pivot_index + 1, right, kindex)
    elif pivot_index > kindex:
        return _find_kth_largest(array, left, pivot_index - 1, kindex)
    else:
        return array[pivot_index]


def _find_kth_largest(array, left, right, kindex):
    pivot_index = -1
    while pivot_index != kindex:
        pivot_index = partition(array, kindex, left, right)
        if pivot_index < kindex:
            left = pivot_index + 1
        elif pivot_index > kindex:
            right = pivot_index - 1
    return array[pivot_index]


def find_kth_largest_element(array, k):
    return _find_kth_largest(array, 0, len(array) - 1, len(array) - k)


def test_find_kth_largest_element():
    assert 1 == find_kth_largest_element([0, 1, 2], 2)
    assert 2 == find_kth_largest_element([0, 1, 3, 2], 2)
    assert 3 == find_kth_largest_element([0, 4, 1, 3, 2], 2)
    assert 0 == find_kth_largest_element([0, 5, 4], 3)
    assert 5 == find_kth_largest_element([5, 0], 1)
    assert 0 == find_kth_largest_element([5, 0], 2)
    assert 2 == find_kth_largest_element([3, 2, 5, 0, 1], 3)
    assert 3 == find_kth_largest_element([3, 2, 5, 0, 1], 2)


def test_partition():
    array = [0, 3, 1, 4]
    assert 3 == partition(array, 3, 0, 3)
    array = [0, 3, 1, 4]
    assert 0 == partition(array, 0, 0, 3)
    array = [0, 3, 1, 4]
    assert 1 == partition(array, 2, 0, 3)
    array = [5, 2, 1]
    assert 2 == partition(array, 0, 0, 2)
    array = [2, 0]
    assert 1 == partition(array, 0, 0, 1)
    array = [2, 0]
    assert 0 == partition(array, 1, 0, 1)
    array = [0]
    assert 0 == partition(array, 0, 0, 0)
