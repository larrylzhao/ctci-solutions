# easy enough. count the multiples of 5

def factorial_zeros(n):
    count = 0
    if (n < 0):
        return -1
    i = 5
    while i <= n:
        count = count + n/i
        i = i * 5

    return count


import unittest

class Test(unittest.TestCase):
    def test_factorial_zeros(self):
        self.assertEqual(factorial_zeros(4), 0)
        self.assertEqual(factorial_zeros(9), 1)
        self.assertEqual(factorial_zeros(10), 2)
        self.assertEqual(factorial_zeros(25), 6)
        self.assertEqual(factorial_zeros(55), 13)

if __name__ == "__main__":
    unittest.main()