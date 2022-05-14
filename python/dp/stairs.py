
def run_up_stairs(n):
    dp = [0, 1, 2, 4] + [0] * (n - 3)
    if n <= 3:
        return dp[n]
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

def test_run_up_stairs():
    assert 1 == run_up_stairs(1)
    assert 2 == run_up_stairs(2)
    assert 4 == run_up_stairs(3)
    assert 7 == run_up_stairs(4)