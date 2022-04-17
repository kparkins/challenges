from linked_list import Node


def get_length_and_tail(node):
    count = 1
    while node.next:
        count += 1
        node = node.next
    return node, count


def overlap(l1, l2):
    tail1, length1 = get_length_and_tail(l1)
    tail2, length2 = get_length_and_tail(l2)
    if tail1 != tail2:
        return None
    short = l1 if length1 <= length2 else l2
    long = l2 if short == l1 else l1
    diff = abs(length1 - length2)
    for _ in range(diff):
        long = long.next
    while long != short:
        short = short.next
        long = long.next
    return short


def test_lists_overlap():
    l1 = Node(1, Node(2, Node(3, Node(4, None))))
    l2 = Node(1, Node(2, Node(3, Node(4, None))))
    assert None == overlap(l1, l2)

    l1.next.next.next = l2
    assert l2 == overlap(l1, l2)

    l1 = Node(1, Node(2, None))
    l2 = Node(2, Node(4, Node(5, None)))
    l2.next.next = l1.next
    assert l1.next == overlap(l2, l1)
