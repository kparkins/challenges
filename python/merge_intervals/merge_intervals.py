from __future__ import print_function
from socket import SO_RCVLOWAT


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    merged = []
    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    current = sorted_intervals[0]
    for i in range(1, len(sorted_intervals)):
        next = sorted_intervals[i]
        if next.start < current.end:
            current.start = min(current.start, next.start)
            current.end = max(current.end, next.end)
        else:
            merged.append(current)
            current = next
    merged.append(current)
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
