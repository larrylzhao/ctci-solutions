import math

def smallest_difference(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return None

    array1 = sorted(array1)
    array2 = sorted(array2)

    smallest_diff = math.abs(array1[0] - array2[0])

    i2 = 0
    for n in array1:


    return smallest_diff

import unittest

class Test(unittest.TestCase):
    def test_smallest_difference(self):
        self.assertEqual(smallest_difference([11, 22, 33, 44], [77, 2, 66, 50]), 6)
        self.assertEqual(smallest_difference([11, 22, 33, 44], [77, 2, 34, 50]), 1)
        self.assertEqual(smallest_difference([11, 77, 33, 44], [77, 2, 34, 50]), 0)
        array1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        array2 = [33, 45, 58, 17]
        self.assertEqual(smallest_difference(array1, array2), 2)
        self.assertEqual(smallest_difference(array2, array1), 2)

if __name__ == "__main__":
    unittest.main()

