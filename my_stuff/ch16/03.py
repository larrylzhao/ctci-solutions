# fairly straightforward. just math

import math

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def dist(self, other):
        if self.x == other.x and self.y == other.y:
            return 0
        return math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )

    def get_coords(self):
        return self.x, self.y


class Segment(object):
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

    def get_length(self):
        return self.p1.dist(self.p2)

    def box_contains(self, p):
        minx, maxx = min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x)
        miny, maxy = min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y)
        return minx <= p.x and maxx >= p.x and miny <= p.y and maxy >= p.y


def intersection(s1, s2):
    a, b = s1.p2.y-




import unittest

class Test(unittest.TestCase):
    def test_intersection(self):
        seg1 = Segment(Point(1,1), Point(4,4))
        seg2 = Segment(Point(3,3), Point(7,7))
        self.assertEqual(intersection(seg1, seg2).coords(), (4,4))
        seg1 = Segment(Point(1,1), Point(4,4))
        seg2 = Segment(Point(5,5), Point(8,8))
        self.assertEqual(intersection(seg1, seg2), None)
        seg1 = Segment(Point(1,1), Point(4,4))
        seg2 = Segment(Point(3,-3), Point(-2,2))
        self.assertEqual(intersection(seg1, seg2), None)
        seg1 = Segment(Point(-1,-1), Point(4,4))
        seg2 = Segment(Point(3,-3), Point(-2,2))
        self.assertEqual(intersection(seg1, seg2).coords(), (0,0))
        seg1 = Segment(Point(0,-1), Point(5,4))
        seg2 = Segment(Point(4,-3), Point(-1,2))
        self.assertEqual(intersection(seg1, seg2).coords(), (1,0))
        seg1 = Segment(Point(0,1), Point(5,6))
        seg2 = Segment(Point(4,-1), Point(-1,4))
        self.assertEqual(intersection(seg1, seg2).coords(), (1,2))
        seg1 = Segment(Point(0,1), Point(10,31))
        seg2 = Segment(Point(0,4.5), Point(10,28.5))
        self.assertEqual(intersection(seg1, seg2).coords(), (35/6.0,18.5))

if __name__ == "__main__":
    unittest.main()
