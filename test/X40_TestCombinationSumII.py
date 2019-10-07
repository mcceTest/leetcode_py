import unittest

from X40_CombinationSumII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        candidates = [10,1,2,7,6,1,5]
        target = 8

        self.assertListEqual(sorted(sol.combinationSum2(candidates, target)), sorted([
                                                                            [1, 7],
                                                                            [1, 2, 5],
                                                                            [2, 6],
                                                                            [1, 1, 6]
                                                                            ]))
       

    def test2(self):
        sol = Solution()
        candidates = [2,5,2,1,2]
        target = 5

        self.assertListEqual(sorted(sol.combinationSum2(candidates, target)), sorted([
                                                                                    [1,2,2],
                                                                                    [5]
                                                                                    ]))
    


if __name__ == "__main__":
    unittest.main()