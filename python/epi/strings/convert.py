
int_string_map = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

string_int_map = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

string_to_hex_map = {
    '0': 0x0,
    '1': 0x1,
    '2': 0x2,
    '3': 0x3,
    '4': 0x4,
    '5': 0x5,
    '6': 0x6,
    '7': 0x7,
    '8': 0x8,
    '9': 0x9,
    'A': 0xA,
    'B': 0xB,
    'C': 0xC,
    'D': 0xD,
    'E': 0xE,
    'F': 0xF
}

hex_to_string_map = {
    0x0: '0',
    0x1: '1',
    0x2: '2',
    0x3: '3',
    0x4: '4',
    0x5: '5',
    0x6: '6',
    0x7: '7',
    0x8: '8',
    0x9: '9',
    0xA: 'A',
    0xB: 'B',
    0xC: 'C',
    0xD: 'D',
    0xE: 'E',
    0xF: 'F',
}


def string_to_int(string):
    if string == '' or string == '-':
        return -1
    result = 0
    for c in string:
        if c not in '+-':
            result = result * 10 + string_int_map[c]
    return -result if string[0] == '-' else result


def int_to_string(integer):
    string = []
    is_negative = integer < 0
    integer = abs(integer)
    while integer != 0:
        digit = integer % 10
        integer //= 10
        string.append(int_string_map[digit])
    if is_negative:
        string.append('-')
    return ''.join(string[::-1])


def convert_number(number, base, nbase):
    def string_int_base(string, base):
        if len(string) < 1:
            return 0
        result = 0
        is_negative = string[0] == '-'
        start = 1 if is_negative else 0
        for c in string[start:]:
            result = result * base + string_to_hex_map[c]
        return -result if is_negative else result
    result = []
    decimal_num = string_int_base(number, base)
    is_negative = decimal_num < 0
    decimal_num = abs(decimal_num)
    while decimal_num > 0:
        digit = decimal_num % nbase
        decimal_num //= nbase
        result.append(hex_to_string_map[digit])
    if is_negative:
        result.append('-')
    return ''.join(result[::-1])


def test_convert_number():
    assert '1' == convert_number('1', 10, 2)
    assert '101' == convert_number('5', 10, 2)
    assert '1010' == convert_number('10', 10, 2)
    assert '1010' == convert_number('A', 16, 2)


def test_string_to_int():
    assert 1 == string_to_int('1')
    assert 123 == string_to_int('123')
    assert 123456 == string_to_int('123456')
    assert -1 == string_to_int('-1')
    assert -123 == string_to_int('-123')
    assert -123456 == string_to_int('-123456')
    assert 1 == string_to_int('+1')
    assert 123456 == string_to_int('+123456')


def test_int_to_string():
    assert '1' == int_to_string(1)
    assert '123' == int_to_string(123)
    assert '1234567' == int_to_string(1234567)
    assert '-1' == int_to_string(-1)
    assert '-123' == int_to_string(-123)
    assert '-1234567' == int_to_string(-1234567)
