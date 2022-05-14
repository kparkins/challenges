import math
import heapq

class Star:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    @property
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __lt__(self, other): 
        return self.distance < other.distance

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z


def compute_closest_stars(stars, k):
    heap = []
    for _ in range(k):
        star = next(stars, None)
        if star is None:
            return heap
        heapq.heappush(heap, (-star.distance, star))
    for star in stars:
        # max heap of the mins
        furthest_distance, furthest_star = heapq.heappop(heap)
        if star.distance < -furthest_distance:
            heapq.heappush(heap, (-star.distance, star))
        else:
            heapq.heappush(heap, (furthest_distance, furthest_star))
    return [s[1] for s in heap]
        

def test_compute_closest_stars():
    stars = [Star(1, 1, 1), Star(2, 2, 2), Star(3, 3, 3)]
    assert [Star(1, 1, 1)] == compute_closest_stars(iter(stars),1)

    stars = [Star(1, 1, 1), Star(2, 2, 2), Star(3, 3, 3)]
    assert sorted(stars[:2]) == sorted(compute_closest_stars(iter(stars),2))

    stars = [Star(1, 1, 1), Star(2, 2, 2), Star(3, 3, 3)]
    assert sorted(stars[:3]) == sorted(compute_closest_stars(iter(stars),3))