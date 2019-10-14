import unittest

from X78_Subsets import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,2,3]
        self.assertListEqual(sorted(sol.subsets(nums)), sorted([
                                                            [3],
                                                            [1],
                                                            [2],
                                                            [1,2,3],
                                                            [1,3],
                                                            [2,3],
                                                            [1,2],
                                                            []
                                                            ]))

    def test2(self):
        sol = Solution()
        nums = [1]
        self.assertListEqual(sorted(sol.subsets(nums)), sorted([
                                                            [1],
                                                            []
                                                            ]))


    


if __name__ == "__main__":
    unittest.main()