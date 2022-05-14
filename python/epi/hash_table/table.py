import collections


def can_write_letter(magazine, text):
    available = collections.Counter(magazine)
    required = collections.Counter(text)
    for c, n in required.items():
        if c not in available or n > available[c]:
            return False
    return True


def test_can_write_letter():
    assert True == can_write_letter("a dog ran", "god")
    assert True == can_write_letter("a dog ran", "go and")
    assert False == can_write_letter("a dog ran", "a cat ran")
