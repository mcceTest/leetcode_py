import unittest
from X120_Triangle import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        triangle = [
                        [2],
                        [3,4],
                    [6,5,7],
                    [4,1,8,3]
                    ]

        self.assertEqual(sol.minimumTotal(triangle), 11)

    def test2(self):
        sol = Solution()
        triangle = [
                        [2]
                    ]

        self.assertEqual(sol.minimumTotal(triangle), 2)

    def test3(self):
        sol = Solution()
        triangle = [
                        [2],
                        [3,4]
                    ]

        self.assertEqual(sol.minimumTotal(triangle), 5)

if __name__ == "__main__":
    unittest.main()