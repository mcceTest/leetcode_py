import unittest
from X118_PascalsTriangle import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        numRows = 5
        self.assertListEqual(sol.generate(numRows), [
                                                        [1],
                                                        [1,1],
                                                    [1,2,1],
                                                    [1,3,3,1],
                                                    [1,4,6,4,1]
                                                    ])

if __name__ == "__main__":
    unittest.main()