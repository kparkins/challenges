from linked_list import Node, equal


def reverse_sublist(L, start, stop):
    if not L or not L.next or start == stop:
        return L
    cursor = L
    head = Node(-1, L)
    prev = head
    left = prev
    for i in range(1, start+1):
        if i < start:
            left = cursor
        prev = cursor
        cursor = cursor.next
    for _ in range(stop - start):
        next = cursor.next
        cursor.next = prev
        prev = cursor
        cursor = next
    left.next.next = cursor
    left.next = prev
    return head.next


def test_reverse_sublist():
    l1 = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    l2 = Node(1, Node(4, Node(3, Node(2, Node(5, None)))))
    assert equal(l2, reverse_sublist(l1, 2, 4))

    l1 = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    l2 = Node(2, Node(1, Node(3, Node(4, Node(5, None)))))
    assert equal(l2, reverse_sublist(l1, 1, 2))

    l1 = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    l2 = Node(5, Node(4, Node(3, Node(2, Node(1, None)))))
    assert equal(l2, reverse_sublist(l1, 1, 5))
