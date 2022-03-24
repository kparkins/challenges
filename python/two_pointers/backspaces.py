
'''
    1. Skip leading backspaces 
        ###xyz

    2. Initialize two pointers
        - One is the runner that is scanning the string
        - The other is the one building the new string with backspaces applied

    Algorithm:

       1 
       x #

       2 
       x _ _

         1
       x #

       _  _  _



       1
       xyz##

       2
       x

        1
       xyz##

        2
       xy  

         1
       xyz##

         2
       xyz 

          1 
       xyz##

        2 
       xy

           1 
       xyz##

       2 
       x

'''


def apply_backspaces(string):
    if len(string) == 0:
        return ""
    result = []
    cursor = 0
    for c in string:
        if c != '#':
            result.append(c)
        if c == '#' and len(result) > 0:
            result.pop()
    return ''.join(result)


def backspace_compare_extra_space(str1, str2):
    return apply_backspaces(str1) == apply_backspaces(str2)


def next_valid_index(string, index):
    backspaces = 0
    while index >= 0:
        if string[index] == '#':
            backspaces += 1
        elif backspaces > 0:
            backspaces -= 1
        else:
            break
        index -= 1
    return index


def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1

    while index1 >= 0 or index2 >= 0:
        i1 = next_valid_index(str1, index1)
        i2 = next_valid_index(str2, index2)
        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if str1[i1] != str2[i2]:
            return False
        index1 = i1 - 1
        index2 = i2 - 1

    return True


if __name__ == '__main__':
    print('Should be true: ', backspace_compare_extra_space('xy#z', 'xzz#'))
    print('Should be false: ', backspace_compare_extra_space('xy#z', 'xyz#'))
    print('Should be true: ', backspace_compare_extra_space('xp#', 'xyz##'))
    print('Should be true: ', backspace_compare_extra_space('xywrrmp', 'xywrrmu#p'))

    print('Should be true: ', backspace_compare('xy#z', 'xzz#'))
    print('Should be false: ', backspace_compare('xy#z', 'xyz#'))
    print('Should be true: ', backspace_compare('xp#', 'xyz##'))
    print('Should be true: ', backspace_compare('xywrrmp', 'xywrrmu#p'))
