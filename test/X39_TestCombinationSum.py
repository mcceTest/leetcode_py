import unittest

from X39_CombinationSum import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        candidates = [2,3,6,7]
        target = 7

        self.assertListEqual(sorted(sol.combinationSum(candidates, target)), sorted([[7], [2, 2, 3]]))
       

    def test2(self):
        sol = Solution()
        candidates = [2,3,5]
        target = 8

        self.assertListEqual(sorted(sol.combinationSum(candidates, target)), sorted([
                                                                                    [2,2,2,2],
                                                                                    [2,3,3],
                                                                                    [3,5]
                                                                                    ]))
    


if __name__ == "__main__":
    unittest.main()