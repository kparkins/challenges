
def all_primes(num):
    if num < 2:
        return []
    primes = []
    is_prime = [False, False] + [True] * (num - 1)
    for i in range(2, num + 1):
        if is_prime[i]:
            for j in range(2 * i, num + 1, i):
                is_prime[j] = False
            primes.append(i)
    return primes


def test_all_primes():
    assert [2, 3] == all_primes(4)
    assert [2, 3, 5, 7, 11, 13, 17] == all_primes(18)
