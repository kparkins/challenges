

def max_profit(prices):
    if len(prices) < 2:
        return 0
    min_index = 0
    max_profit = 0
    for current_index in range(1, len(prices)):
        if prices[current_index] < prices[min_index]:
            min_index = current_index
        max_profit = max(max_profit, prices[current_index] - prices[min_index])
    return max_profit


def max_profit_div(prices):
    return _max_profit_div(prices, 0, len(prices)-1)


def _max_profit_div(prices, low, high):
    if low == high:
        return 0
    mid = (high - low) // 2 + low
    left_profit = _max_profit_div(prices, low, mid)
    right_profit = _max_profit_div(prices, mid+1, high)
    mid_profit = max(prices[mid+1:high+1]) - min(prices[low:mid+1])
    return max(left_profit, max(mid_profit, right_profit))


def test_max_profit():
    assert 0 == max_profit([1])
    assert 2 == max_profit([2, 4])
    assert 4 == max_profit([2, 5, 1, 5])
    assert 30 == max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])


def test_max_profit_div():
    assert 0 == max_profit_div([1])
    assert 2 == max_profit_div([2, 4])
    assert 4 == max_profit_div([2, 5, 1, 5])
    assert 30 == max_profit_div(
        [310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
