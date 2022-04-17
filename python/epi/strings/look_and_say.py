
def look_and_say(number):
    if number <= 1:
        return '1'
    current_result = ['1']
    for _ in range(number-1):
        count = 0
        digit = current_result[0]
        next_result = []
        for i in range(0, len(current_result)):
            if current_result[i] != digit:
                next_result.extend([str(count), digit])
                digit = current_result[i]
                count = 1
            else:
                count += 1
        next_result.extend([str(count), digit])
        current_result = next_result
    return ''.join(current_result)


def test_look_and_say():
    assert '1' == look_and_say(1)
    assert '11' == look_and_say(2)
    assert '21' == look_and_say(3)
    assert '1211' == look_and_say(4)
    assert '111221' == look_and_say(5)
    assert '312211' == look_and_say(6)
