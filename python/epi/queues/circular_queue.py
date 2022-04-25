
class CircularQueue:

    def __init__(self, capacity):
        self._data = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def enqueue(self, element):
        if self._size == len(self._data):
            self._expand()
        self._data[self._tail] = element
        self._tail = self._index(self._tail + 1)
        self._size += 1

    def dequeue(self):
        element = self._data[self._head]
        self._head = self._index(self._head + 1)
        self._size -= 1
        return element

    def size(self):
        return self._size

    def _index(self, i):
        return i % len(self._data)

    def _expand(self):
        new_data = [None] * (len(self._data) * 2)
        for i in range(self._size):
            new_data[i] = self._data[self._head]
            self._head = self._index(self._head + 1)
        self._data = new_data
        self._head = 0
        self._tail = self._size


def test_circular_queue():
    q = CircularQueue(1)
    q.enqueue(1)
    assert q.size() == 1
    assert q.dequeue() == 1
    assert q.size() == 0

    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.dequeue() == 1
    assert q.dequeue() == 2

    for i in range(10):
        q.enqueue(i)

    for i in range(10):
        assert q.dequeue() == i
