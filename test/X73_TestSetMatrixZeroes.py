import unittest

from X73_SetMatrixZeroes import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        matrix = [
                [1,1,1],
                [1,0,1],
                [1,1,1]
                ]

        sol.setZeroes(matrix)

        self.assertListEqual(matrix, [
                                        [1,0,1],
                                        [0,0,0],
                                        [1,0,1]
                                        ])


    def test2(self):
        sol = Solution()
        matrix = [
                [0,1,2,0],
                [3,4,5,2],
                [1,3,1,5]
                ]

        sol.setZeroes(matrix)

        self.assertListEqual(matrix, [
                                    [0,0,0,0],
                                    [0,4,5,0],
                                    [0,3,1,0]
                                    ])
    

       
if __name__ == "__main__":
    unittest.main()