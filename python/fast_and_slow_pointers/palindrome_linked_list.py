
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# 1 2 1 None
# 1 2 1 1 None
# 1 1
def _find_middle_element(node):
    fast, slow = node, node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# 2 -> 4 -> 4 <- 2
def _check_palindrome(head, tail):
    left, right = head, tail
    while left != right:
        if left.value != right.value:
            return False
        if left.next == right:
            break
        left = left.next
        right = right.next
    return True


def _reverse_links(start, stop=None):
    prev = start
    cursor = start.next
    while cursor != stop:
        next = cursor.next
        cursor.next = prev
        prev = cursor
        cursor = next
    return prev


def is_palindromic_linked_list(head):
    middle = _find_middle_element(head)
    end = _reverse_links(middle)
    is_palidrome = _check_palindrome(head, end)
    _reverse_links(end, middle)
    return is_palidrome


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


if __name__ == '__main__':
    main()
