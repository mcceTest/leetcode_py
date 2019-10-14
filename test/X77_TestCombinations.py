import unittest

from X77_Combinations import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 4
        k = 2
        self.assertListEqual(sorted(sol.combine(n, k)), sorted([
                                [2,4],
                                [3,4],
                                [2,3],
                                [1,2],
                                [1,3],
                                [1,4],
                                ]))


    def test2(self):
        sol = Solution()
        n = 4
        k = 2
        self.assertListEqual(sorted(sol.combine(n, k)), sorted([
                                [2,4],
                                [3,4],
                                [2,3],
                                [1,2],
                                [1,3],
                                [1,4],
                                ]))

    


if __name__ == "__main__":
    unittest.main()