class Node:

    def __init__(self, val, next):
        self.next = next
        self.val = val


def length(l):
    cursor = l
    length = 0
    while cursor != None:
        length += 1
        cursor = cursor.next
    return length


def elements_in_order(l):
    cursor = l.next
    prev = l
    while cursor != None:
        if cursor.val < prev.val:
            return False
        prev = cursor
        cursor = cursor.next
    return True


def equal(l1, l2):
    if length(l1) != length(l2):
        return False
    while l1 is not None and l2 is not None:
        if l1.val != l2.val:
            return False
        l1, l2, = l1.next, l2.next
    return True
