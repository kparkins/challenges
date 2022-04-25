
from contextlib import AsyncExitStack


class QueueOfStacks:

    def __init__(self):
        self._left = []
        self._right = []

    def enqueue(self, element):
        if self._in_dequeue_state():
            self._swap_state(self._right, self._left)
        self._left.append(element)

    def dequeue(self):
        if not self._in_dequeue_state():
            self._swap_state(self._left, self._right)
        return self._right.pop()

    def size(self):
        return max(len(self._left), len(self._right))

    def _in_dequeue_state(self):
        return len(self._right) > 0 and len(self._left) == 0

    def _swap_state(self, src, dst):
        while len(src) > 0:
            dst.append(src.pop())


def test_queue_of_stacks():
    q = QueueOfStacks()

    q.enqueue(1)
    assert q.size() == 1
    assert q.dequeue() == 1

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

    for i in range(10):
        q.enqueue(i)
    for i in range(10):
        assert q.dequeue() == i

    try:
        q.dequeue()
        assert False
    except:
        assert True
