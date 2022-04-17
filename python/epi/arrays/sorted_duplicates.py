

def remove_duplicates(array):
    if len(array) <= 1:
        return len(array)
    window_index = 1
    for cursor in range(1, len(array)):
        if array[cursor] != array[cursor - 1]:
            array[window_index] = array[cursor]
            window_index += 1
    return window_index


def test_remove_duplicates():
    val = [0]
    assert 1 == remove_duplicates(val)
    assert [0] == val

    val = [-1, -1, 0, 0, 4, 5]
    assert 4 == remove_duplicates(val)
    assert [-1, 0, 4, 5] == val[0:4]

    val = [1, 1, 1, 1]
    assert 1 == remove_duplicates(val)
    assert [1] == val[0:1]

    val = [0, 0, 0, 0, 5]
    assert 2 == remove_duplicates(val)
    assert [0, 5] == val[0:2]

    val = [1,  2, 2, 3, 3]
    assert 3 == remove_duplicates(val)
    assert [1, 2, 3] == val[0:3]
