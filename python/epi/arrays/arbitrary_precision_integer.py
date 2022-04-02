

from math import remainder
from types import new_class
from unicodedata import digit


def increment_integer(digits):
    if len(digits) < 1:
        return digits
    val = digits[len(digits) - 1] + 1
    carry = val // 10
    digits[len(digits) - 1] = val % 10
    for i in range(len(digits) - 2, -1, -1):
        new_val = digits[i] + carry
        carry = new_val // 10
        digits[i] = new_val % 10
    remainder = []
    while carry > 0:
        remainder.append(carry % 10)
        carry //= 10
    return list(reversed(remainder)) + digits


def test_increment_integer():
    assert [1] == increment_integer([0])
    assert [1, 3, 0] == increment_integer([1, 2, 9])
    assert [1, 3, 1] == increment_integer([1, 3, 0])
    assert [1, 0, 0, 0, 0, 0, 0] == increment_integer([9, 9, 9, 9, 9, 9])
