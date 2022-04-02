import math


def is_sudoku_valid(board):
    def _is_valid(seq):
        seq = list(filter(lambda x: x != 0, seq))
        return len(seq) == len(set(seq))

    def _are_rows_valid(board):
        return all(
            _is_valid([
                board[row][col] for col in range(len(board[0]))
            ])
            for row in range(len(board))
        )

    def _are_columns_valid(board):
        return all(
            _is_valid([
                board[row][col] for row in range(len(board))
            ])
            for col in range(len(board[0]))
        )

    def _are_subarrays_valid(board):
        n = int(math.sqrt(len(board)))
        return all(
            _is_valid([
                board[row][col]
                for row in range(i * n, (i + 1) * n)
                for col in range(j * n, (j + 1) * n)
            ])
            for i in range(n)
            for j in range(n)
        )

    return _are_rows_valid(board) and \
        _are_columns_valid(board) and \
        _are_subarrays_valid(board)


def test_is_sudoku_valid():
    assert True == is_sudoku_valid([
        [0, 0, 1],
        [3, 5, 0],
        [4, 0, 0]
    ])

    assert False == is_sudoku_valid([
        [0, 0, 1],
        [3, 5, 5],
        [4, 0, 0]
    ])

    assert True == is_sudoku_valid([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    assert False == is_sudoku_valid([
        [5, 3, 6, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    assert False == is_sudoku_valid([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 1, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    assert False == is_sudoku_valid([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 8, 7, 9]
    ])
