
def partition(array, index):
    pivot = array[index]
    low, high = 0, len(array)
    cursor = 0
    while cursor < high:
        if array[cursor] < pivot:
            array[low], array[cursor] = array[cursor], array[low]
            low += 1
            cursor += 1
        elif array[cursor] > pivot:
            high -= 1
            array[high], array[cursor] = array[cursor], array[high]
        else:
            cursor += 1
    return array


def test_partition():
    assert [0, 0, 1, 1, 2, 2] == partition([2, 0, 1, 2, 1, 0], 2)
    assert [0, 0, 2, 1, 1, 2] == partition([2, 0, 1, 2, 1, 0], 1)
    assert [0, 1, 1, 1, 1, 1] == partition([1, 1, 1, 1, 1, 0], 1)