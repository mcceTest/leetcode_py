import unittest
from X190_ReverseBits import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 43261596
        self.assertEqual(sol.reverseBits(n), 964176192)

    def test2(self):
        sol = Solution()
        n = 4294967293
        self.assertEqual(sol.reverseBits(n), 3221225471)

if __name__ == "__main__":
    unittest.main()