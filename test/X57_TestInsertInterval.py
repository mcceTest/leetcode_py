import unittest

from X57_InsertInterval import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]

        self.assertListEqual(sol.insert(intervals, newInterval), [[1,5],[6,9]])
    

    def test2(self):
        sol = Solution()
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]

        self.assertListEqual(sol.insert(intervals, newInterval), [[1,2],[3,10],[12,16]])

    def test3(self):
        sol = Solution()
        intervals = []
        newInterval = [5,7]

        self.assertListEqual(sol.insert(intervals, newInterval), [[5,7]])
    
       
if __name__ == "__main__":
    unittest.main()