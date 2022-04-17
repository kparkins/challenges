

# replace each a by two d's
# remove each b
def replace_and_remove(string):
    def calculate_new_length(string):
        new_size = len(string)
        for c in string:
            if c == 'b':
                new_size -= 1
            elif c == 'a':
                new_size += 2
        return new_size

    new_length = calculate_new_length(string)
    if new_length == 0:
        return ''
    old_length = len(string)
    string.extend([''] * (new_length - len(string)))
    write_index = new_length
    for i in range(old_length-1, -1, -1):
        if string[i] == 'b':
            continue
        elif string[i] == 'a':
            write_index -= 2
            string[write_index] = 'd'
            string[write_index + 1] = 'd'
        else:
            write_index -= 1
            string[write_index] = string[i]
    return "".join(string[write_index:])


def test_replace_and_remove():
    assert "" == replace_and_remove(list('b'))
    assert "dd" == replace_and_remove(list('a'))
    assert "ddcd" == replace_and_remove(list('abcd'))
    assert "dcdd" == replace_and_remove(list('dbca'))
