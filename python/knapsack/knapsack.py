
'''def _solve_knapsack_memo(memo, profits, weights, capacity, index):
    if capacity <= 0 or index >= len(weights):
        return 0
    if memo[index][capacity] != -1:
        return memo[index][capacity]
    profit1 = 0
    if capacity - weights[index] >= 0:
        profit1 = profits[index] + _solve_knapsack_memo(
            memo, profits, weights, capacity - weights[index], index + 1)
    profit2 = _solve_knapsack_memo(memo, profits, weights, capacity, index + 1)
    memo[index][capacity] = max(profit1, profit2)
    return memo[index][capacity]


def _solve_knapsack(profits, weights, capacity, index):
    if capacity <= 0 or index >= len(weights):
        return 0
    profit1 = 0
    if capacity - weights[index] >= 0:
        profit1 = profits[index] + _solve_knapsack(
            profits, weights, capacity - weights[index], index + 1)
    profit2 = _solve_knapsack(profits, weights, capacity, index + 1)
    return max(profit1, profit2)


def solve_knapsack(profits, weights, capacity):
    memo = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return _solve_knapsack_memo(memo, profits, weights, capacity, 0)


def solve_knapsack_dp(profits, weights, capacity):
    dp = [[0 for x in range(capacity + 1)] for y in range(len(profits))]
    for c in range(len(dp[0])):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for j in range(len(dp)):
        dp[j][0] = 0
    n = len(profits)
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            profit1 = dp[i-1][c]
            if weights[i] <= c:
                profit2 = profits[i] + dp[i - 1][c - weights[i]]
            dp[i][c] = max(profit1, profit2)
    return dp[n - 1][capacity]'''


def _solve_knapsack(profits, weights, capacity, index):
    if index >= len(weights):
        return 0

    excluded = _solve_knapsack(profits, weights, capacity, index + 1)
    included = 0
    if capacity - weights[index] >= 0:
        included = profits[index] + _solve_knapsack(
            profits, weights, capacity - weights[index], index + 1)
    return max(included, excluded)


def solve_knapsack(profits, weights, capacity):
    return _solve_knapsack(profits, weights, capacity, 0)


def solve_knapsack_dp(profits, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if j - weights[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                included = profits[i - 1] + dp[i - 1][j - weights[i - 1]]
                excluded = dp[i - 1][j]
                dp[i][j] = max(included, excluded)
    return dp[len(weights)][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(' ----- ')
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
