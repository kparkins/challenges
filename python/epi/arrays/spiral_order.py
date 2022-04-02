
# loop to row max
# loop to column max
# loop to row min
# loop to column min
# recurse on smaller matrix
# 1       1       1        2
def spiral_order(matrix):
    ordering = []
    row_min, row_max, col_min, col_max = 0, len(
        matrix) - 1, 0, len(matrix[0]) - 1
    while row_min <= row_max and col_min <= col_max:
        for c in range(col_min, col_max + 1):
            ordering.append(matrix[row_min][c])
        row_min += 1
        for r in range(row_min, row_max + 1):
            ordering.append(matrix[r][col_max])
        col_max -= 1
        if row_min <= row_max:
            for c in range(col_max, col_min - 1, -1):
                ordering.append(matrix[row_max][c])
            row_max -= 1
        if col_min <= col_max:
            for r in range(row_max, row_min - 1, -1):
                ordering.append(matrix[r][col_min])
            col_min += 1
    return ordering


def spiral_order_optimized(matrix):
    ordering = []
    row_min, row_max, col_min, col_max = 0, len(
        matrix) - 1, 0, len(matrix[0]) - 1
    while row_min <= row_max and col_min <= col_max:
        ordering.extend([matrix[row_min][c]
                        for c in range(col_min, col_max + 1)])
        row_min += 1
        ordering.extend(matrix[r][col_max]
                        for r in range(row_min, row_max + 1))
        col_max -= 1
        if row_min <= row_max:
            ordering.extend([matrix[row_max][c]
                            for c in range(col_max, col_min - 1, -1)])
            row_max -= 1
        if col_min <= col_max:
            ordering.extend([matrix[r][col_min]
                            for r in range(row_max, row_min - 1, -1)])
            col_min += 1
    return ordering


def test_spiral_order():
    assert [0, 1, 2, 3] == spiral_order([[0, 1], [3, 2]])
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8] == spiral_order([
        [0, 1, 2],
        [7, 8, 3],
        [6, 5, 4]
    ])
    assert [0, 1, 2, 3, 4, 5] == spiral_order([
        [0, 1],
        [5, 2],
        [4, 3]
    ])
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] == spiral_order([
        [0, 1, 2, 3],
        [9, 10, 11, 4],
        [8, 7, 6, 5]
    ])
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] == spiral_order([
        [0, 1, 2],
        [9, 10, 3],
        [8, 11, 4],
        [7, 6, 5],
    ])

    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] == spiral_order([
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    ])
