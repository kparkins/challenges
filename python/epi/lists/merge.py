from linked_list import Node, elements_in_order, length, equal


def merge(l1, l2):
    new_list = Node(-1, None)
    new_cursor = new_list
    while l1 and l2:
        if l1.val < l2.val:
            new_cursor.next, l1 = l1, l1.next
        else:
            new_cursor.next, l2 = l2, l2.next
        new_cursor = new_cursor.next
    if l1:
        new_cursor.next = l1
    elif l2:
        new_cursor.next = l2
    return new_list.next


def even_odd_merge(node):
    if not node or not node.next:
        return node
    flag = 0
    cursor = node
    even_head, odd_head = Node(-1, None), Node(-1, None)
    even_tail, odd_tail = even_head, odd_head
    while cursor:
        if flag:
            odd_tail.next = cursor
            odd_tail = odd_tail.next
        else:
            even_tail.next = cursor
            even_tail = even_tail.next
        flag ^= 1
        cursor = cursor.next
    odd_tail.next = None
    even_tail.next = odd_head.next
    return even_head.next


def test_elements_in_order():
    l = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    assert elements_in_order(l)

    l = Node(1, Node(2, Node(4, Node(4, Node(5, None)))))
    assert elements_in_order(l)

    l = Node(1, Node(2, Node(5, Node(4, Node(5, None)))))
    assert not elements_in_order(l)


def test_length():
    l = None
    assert 0 == length(l)

    l = Node(1, None)
    assert 1 == length(l)

    l = Node(1, Node(2, Node(5, Node(4, Node(5, None)))))
    assert 5 == length(l)


def test_merge():
    l1 = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    l2 = Node(6, Node(7, Node(8, Node(9, Node(10, None)))))
    merged = merge(l1, l2)
    assert elements_in_order(merged)
    assert 10 == length(merged)

    l1 = Node(1, Node(3, Node(5, None)))
    l2 = Node(2, Node(4, Node(6, None)))
    merged = merge(l1, l2)
    assert elements_in_order(merged)
    assert 6 == length(merged)

    l1 = Node(1, Node(3, Node(5, None)))
    l2 = Node(2, Node(4, Node(6, None)))
    merged = merge(l2, l1)
    assert elements_in_order(merged)
    assert 6 == length(merged)

    l1 = Node(1, Node(3, Node(5, None)))
    l2 = Node(1, None)
    merged = merge(l2, l1)
    assert elements_in_order(merged)
    assert 4 == length(merged)

    l1 = Node(6, None)
    l2 = Node(1, Node(3, Node(5, None)))
    merged = merge(l1, l2)
    assert elements_in_order(merged)
    assert 4 == length(merged)


def test_even_odd_merge():
    nodes = Node(1, None)
    result = Node(1, None)
    assert equal(result, even_odd_merge(nodes))

    nodes = Node(1, Node(3, Node(5, Node(7, None))))
    result = Node(1, Node(5, Node(3, Node(7, None))))
    assert equal(result, even_odd_merge(nodes))

    nodes = Node(0, Node(1, Node(2, Node(3, Node(4, None)))))
    result = Node(0, Node(2, Node(4, Node(1, Node(3, None)))))
    assert equal(result, even_odd_merge(nodes))
