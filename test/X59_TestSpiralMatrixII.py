import unittest

from X59_SpiralMatrixII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 3
    
        self.assertListEqual(sol.generateMatrix(n), [
                                                    [ 1, 2, 3 ],
                                                    [ 8, 9, 4 ],
                                                    [ 7, 6, 5 ]
                                                    ])

    def test2(self):
        sol = Solution()
        n = 2
    
        self.assertListEqual(sol.generateMatrix(n), [
                                                    [ 1, 2 ],
                                                    [ 4, 3 ],
                                                    ])

    def test3(self):
        sol = Solution()
        n = 1
    
        self.assertListEqual(sol.generateMatrix(n), [
                                                    [ 1],
                                                    ])
   
    
       
if __name__ == "__main__":
    unittest.main()