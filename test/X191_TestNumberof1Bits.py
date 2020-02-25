import unittest
from X191_Numberof1Bits import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 0b00000000000000000000000000001011
        self.assertEqual(sol.hammingWeight(n), 3)

    def test2(self):
        sol = Solution()
        n = 0b00000000000000000000000010000000
        self.assertEqual(sol.hammingWeight(n), 1)

    def test3(self):
        sol = Solution()
        n = 0b11111111111111111111111111111101
        self.assertEqual(sol.hammingWeight(n), 31)

    

if __name__ == "__main__":
    unittest.main()