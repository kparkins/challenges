

from multiprocessing.sharedctypes import Value


class MaxStack:

    def __init__(self):
        self._elements = []
        self._current_max = None

    def pop(self):
        value, _ = self._elements.pop()
        if len(self._elements) == 0:
            self._current_max = None
        else:
            self._current_max = self._elements[-1][1]
        return value

    def peek(self):
        element = self.elements[-1]
        return element[0]

    def push(self, value):
        element = (value, self._current_max)
        if self._current_max is None or value > self._current_max:
            element = (value, value)
            self._current_max = value
        self._elements.append(element)

    def max(self):
        if self._current_max is None:
            raise ValueError()
        return self._current_max


def evaluate_rpn(expression):
    parts = expression.split(',')
    if len(parts) == 1:
        return int(parts[0])
    elif len(parts) < 3:
        raise ValueError()
    stack = []
    for part in parts:
        part = part.strip()
        if part.strip('-').isnumeric():
            stack.append(int(part))
            continue

        op2 = stack.pop()
        op1 = stack.pop()
        if part == '-':
            stack.append(op1 - op2)
        elif part == '+':
            stack.append(op1 + op2)
        elif part == '*':
            stack.append(op1 * op2)
        elif part == '/':
            stack.append(op1 // op2)
    return stack[0]


def valid_parenthesis(string):
    mapping = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    stack = []
    for c in string:
        if c in mapping:
            stack.append(c)
        elif len(stack) == 0 or not mapping[stack.pop()] == c:
            return False
    return len(stack) == 0


def test_max_stack():
    m = MaxStack()

    m.push(1)
    assert m.max() == 1
    m.push(2)
    assert m.max() == 2
    m.push(1)
    assert m.max() == 2
    m.push(3)
    assert m.max() == 3
    m.pop()
    assert m.max() == 2
    m.pop()
    assert m.max() == 2
    m.pop()
    assert m.max() == 1

    try:
        m.pop()
        assert False
    except:
        assert True


def test_evaluate_rpn():
    assert 3 == evaluate_rpn('1,2,+')
    assert 1 == evaluate_rpn('-1,2,+')
    assert 1 == evaluate_rpn('2, 1, -')
    assert 6 == evaluate_rpn('2,3,*')
    assert -6 == evaluate_rpn('2,-3,*')
    assert 2 == evaluate_rpn('6,3,/')
    assert -2 == evaluate_rpn('-6,3,/')
    assert 15 == evaluate_rpn('3,4,+,2,*,1,+')


def test_valid_parenthesis():

    assert True == valid_parenthesis('()')
    assert False == valid_parenthesis('(')
    assert True == valid_parenthesis('{()()}')
    assert False == valid_parenthesis('{()()})')
    assert False == valid_parenthesis('{()(})')
    assert False == valid_parenthesis('[{]()()}')
    assert True == valid_parenthesis('[{{}()[]([])}]')
    assert False == valid_parenthesis('[[[[[]]]')
