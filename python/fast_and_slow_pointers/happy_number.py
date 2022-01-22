def _next_step(num):
    result = 0
    while num > 0:
        result += (num % 10) ** 2
        num //= 10
    return result


def find_happy_number(num):
    slow, fast = num, _next_step(num)
    while slow != fast:
        slow = _next_step(slow)
        fast = _next_step(_next_step(fast))
    return slow == 1


def main():
    #print(_next_step(12))
    print(find_happy_number(23))
    print(find_happy_number(12))


if __name__ == '__main__':
    main()
