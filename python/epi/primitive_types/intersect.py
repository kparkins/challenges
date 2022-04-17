from collections import namedtuple

Rectangle = namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(a, b):
    def intersects(a, b):
        return (a.x + a.width >= b.x and a.x <= b.x + b.width) or \
               (a.y + a.height >= b.y and a.y <= b.y + b.height)
    if not intersects(a, b):
        return None
    return Rectangle(
        max(a.x, b.x), 
        max(a.y, b.y),
        min(a.x + a.width, b.x + b.width) - max(a.x, b.x),
        min(a.y + a.height, b.y + b.height) - max(a.y, b.y),
    )

    
