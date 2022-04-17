
def is_palindromic(string):
    left, right = 0, len(string) - 1
    while left <= right:
        if not string[left].isalnum():
            left += 1
        elif not string[right].isalnum():
            right -= 1
        elif string[left].lower() != string[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def test_is_palindromic():
    assert False == is_palindromic('Ray a ray')
    assert True == is_palindromic('Able was I, ere I saw Elba')
    assert True == is_palindromic('A man, a plan, a canal, panama')
