

def reverse_words(string):
    def reverse_range(string, left, right):
        while left < right:
            string[left], string[right] = string[right], string[left]
            left, right = left + 1, right - 1
    reverse_range(string, 0, len(string) - 1)
    start = 0
    while start < len(string):
        cursor = start
        while cursor < len(string) and string[cursor] != ' ':
            cursor += 1
        reverse_range(string, start, cursor - 1)
        start = cursor + 1
    reverse_range(string, start, len(string) - 1)
    return string


def test_reverse_words():
    assert list("dog cat") == reverse_words(list("cat dog"))
    assert list("dog cat cow") == reverse_words(list("cow cat dog"))
    assert list("beach the to went I") == reverse_words(
        list("I went to the beach"))
