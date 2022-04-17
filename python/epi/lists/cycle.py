from linked_list import Node


def _cycle_length(node):
    count = 1
    runner = node.next
    while runner != node:
        runner = runner.next
        count += 1
    return count


def _find_cycle_start(head, cycle_length):
    behind, ahead = head, head
    for _ in range(cycle_length):
        ahead = ahead.next
    while behind != ahead:
        behind = behind.next
        ahead = ahead.next
    return behind


def has_cycle(head):
    slow, fast = head, head.next
    while fast and fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    if slow != fast:
        return None
    return _find_cycle_start(head, _cycle_length(slow))


def test_has_cycle():
    n5 = Node(5, None)
    l1 = Node(1, Node(2, Node(3, Node(4, n5))))
    n5.next = l1
    assert 1 == has_cycle(l1).val

    n2 = Node(2, Node(3, Node(4, None)))
    n2.next.next.next = n2
    l1 = Node(1, n2)
    assert 2 == has_cycle(l1).val

    n1 = Node(1, None)
    n1.next = n1
    assert 1 == has_cycle(n1).val
