
from collections import defaultdict


def parity_naive(bits):
    parity = 0
    for _ in range(0, 64):
        parity ^= bits & 0x1
        bits = bits >> 1
    return parity


def parity_fast(bits):
    bits ^= bits >> 32
    bits ^= bits >> 16
    bits ^= bits >> 8
    bits ^= bits >> 4
    bits ^= bits >> 2
    bits ^= bits >> 1
    return bits & 0x1


def parity_lookup(precomputed, bits):
    chunk_size = 16
    bit_mask = 0xffff
    return precomputed[(bits >> 3 * chunk_size) & bit_mask] ^ \
        precomputed[(bits >> 2 * chunk_size) & bit_mask] ^ \
        precomputed[(bits >> 1 * chunk_size) & bit_mask] ^ \
        precomputed[bits & bit_mask]


def propagate_rightmost_bit(bits):
    return bits | (bits - 1)


def mod_power_of_two(x, p):
    return x & (p - 1)


# 1 2 4 8 16 32 64 128 256
def is_power_of_two(bits):
    return bits & (bits - 1) == 0


def fast_pow_recursive(x, y):
    if y < 0:
        return 1 / _fast_pow(x, -y)
    return _fast_pow(x, y)


def _fast_pow(x, y):
    if y == 0:
        return 1
    sub_result = fast_pow(x, y >> 1)
    sub_result *= sub_result
    return x * sub_result if y & 1 else sub_result


def fast_pow_memo(x, y):
    mem = defaultdict(int)
    mem[0] = 1
    if y < 0:
        return 1 / _fast_pow_memo(mem, x, -y)
    res = _fast_pow_memo(mem, x, y)
    return res


def _fast_pow_memo(mem, x, y):
    if y in mem:
        return mem[y]
    sub_result = _fast_pow_memo(mem, x, y >> 1)
    sub_result *= sub_result
    if y & 1:
        sub_result *= x
    mem[y] = sub_result
    return sub_result


def fast_pow(x, y):
    result, power = 1, y
    if y < 0:
        power, x = -power, 1 / x
    while power:
        if power & 1:
            result *= x
        x = x * x
        power >>= 1
    return result


def test_fast_pow():
    assert 2**1 == fast_pow(2, 1)
    assert 2**2 == fast_pow(2, 2)
    assert 2**3 == fast_pow(2, 3)
    assert 2**4 == fast_pow(2, 4)
    assert 2**5 == fast_pow(2, 5)
    assert 3**1 == fast_pow(3, 1)
    assert 3**2 == fast_pow(3, 2)
    assert 3**3 == fast_pow(3, 3)
    assert 3**4 == fast_pow(3, 4)
    assert 3**5 == fast_pow(3, 5)


def test_fast_pow_memo():
    assert 2**1 == fast_pow_memo(2, 1)
    assert 2**2 == fast_pow_memo(2, 2)
    assert 2**3 == fast_pow_memo(2, 3)
    assert 2**4 == fast_pow_memo(2, 4)
    assert 2**5 == fast_pow_memo(2, 5)
    assert 3**1 == fast_pow_memo(3, 1)
    assert 3**2 == fast_pow_memo(3, 2)
    assert 3**3 == fast_pow_memo(3, 3)
    assert 3**4 == fast_pow_memo(3, 4)
    assert 3**5 == fast_pow_memo(3, 5)


def test_fast_pow_recursive():
    assert 2**1 == fast_pow_recursive(2, 1)
    assert 2**2 == fast_pow_recursive(2, 2)
    assert 2**3 == fast_pow_recursive(2, 3)
    assert 2**4 == fast_pow_recursive(2, 4)
    assert 2**5 == fast_pow_recursive(2, 5)
    assert 3**1 == fast_pow_recursive(3, 1)
    assert 3**2 == fast_pow_recursive(3, 2)
    assert 3**3 == fast_pow_recursive(3, 3)
    assert 3**4 == fast_pow_recursive(3, 4)
    assert 3**5 == fast_pow_recursive(3, 5)


def test_parity_naive():
    assert 1 == parity_naive(0b1)
    assert 0 == parity_naive(0b0)
    assert 0 == parity_naive(0b1010)
    assert 1 == parity_naive(0b1011)
    assert 0 == parity_naive(0b10100000010001)
    assert 1 == parity_naive(0b10100100010001)


def test_parity_fast():
    assert 1 == parity_fast(0b1)
    assert 0 == parity_fast(0b0)
    assert 0 == parity_fast(0b1010)
    assert 1 == parity_fast(0b1011)
    assert 0 == parity_fast(0b10100000010001)
    assert 1 == parity_fast(0b10100100010001)


def test_parity_lookup():
    # assuming 64 bit integers
    precomputed = [parity_fast(i) for i in range(2**16)]
    assert 1 == parity_lookup(precomputed, 0b1)
    assert 0 == parity_lookup(precomputed, 0b0)
    assert 0 == parity_lookup(precomputed, 0b1010)
    assert 1 == parity_lookup(precomputed, 0b1011)
    assert 0 == parity_lookup(precomputed, 0b10100000010001)
    assert 1 == parity_lookup(precomputed, 0b10100100010001)


def test_propagate_rightmost_bits():
    assert 0b11 == propagate_rightmost_bit(0b10)
    assert 0b10111 == propagate_rightmost_bit(0b10100)
    assert 0b11111 == propagate_rightmost_bit(0b10000)
    assert 0b11011 == propagate_rightmost_bit(0b11010)


def test_mod_power_of_two():
    assert 13 == mod_power_of_two(77, 64)
    assert 1 == mod_power_of_two(5, 4)
    assert 3 == mod_power_of_two(15, 4)


def test_is_power_of_two():
    assert False == is_power_of_two(92)
    assert False == is_power_of_two(82)
    assert False == is_power_of_two(3)
    assert True == is_power_of_two(2)
    assert True == is_power_of_two(1)
    assert True == is_power_of_two(128)
