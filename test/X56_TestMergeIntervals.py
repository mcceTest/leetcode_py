import unittest

from X56_MergeIntervals import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        intervals = [[1,3],[2,6],[8,10],[15,18]]

        self.assertListEqual(sorted(sol.merge(intervals)), sorted( [[1,6],[8,10],[15,18]]))
    

    def test2(self):
        sol = Solution()
        intervals =[[1,4],[4,5]]

        self.assertListEqual(sorted(sol.merge(intervals)), sorted( [[1,5]]))
    
       
if __name__ == "__main__":
    unittest.main()