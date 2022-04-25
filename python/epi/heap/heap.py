import heapq


def merge_sorted_arrays(arrays):
    heap = []
    array_iters = [iter(a) for a in arrays]
    for i, it in enumerate(array_iters):
        element = next(it, None)
        if element is not None:
            heapq.heappush(heap, (element, i))
    ordered_array = []
    while len(heap) > 0:
        min_element, index = heapq.heappop(heap)
        ordered_array.append(min_element)
        next_element = next(array_iters[index], None)
        if next_element is not None:
            heapq.heappush(heap, (next_element, index))
    return ordered_array


def test_merge_sorted_arrays():
    arrays = [
        [1, 2, 4],
        [0, 3, 5, 7],
        [6]
    ]
    assert [0, 1, 2, 3, 4, 5, 6, 7] == merge_sorted_arrays(arrays)
