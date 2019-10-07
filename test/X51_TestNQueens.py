import unittest

from X51_NQueens import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 4
        print(sol.solveNQueens(n))

        self.assertListEqual(sorted(sol.solveNQueens(n)), sorted([
                                                                [".Q..",  
                                                                "...Q",
                                                                "Q...",
                                                                "..Q."],

                                                                ["..Q.",  
                                                                "Q...",
                                                                "...Q",
                                                                ".Q.."]
                                                                ]))


    def test2(self):
        sol = Solution()
        n = 1
        print(sol.solveNQueens(n))

        self.assertListEqual(sorted(sol.solveNQueens(n)), sorted([
                                                                ["Q"]  
                                                                ]))

    
    
       
if __name__ == "__main__":
    unittest.main()