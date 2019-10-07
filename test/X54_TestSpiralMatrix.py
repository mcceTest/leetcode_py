import unittest

from X54_SpiralMatrix import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        matrix = [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]
                ]

        self.assertListEqual(sol.spiralOrder(matrix), [1,2,3,6,9,8,7,4,5])
    
    def test2(self):
        sol = Solution()
        matrix = [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9,10,11,12]
                    ]

        self.assertListEqual(sol.spiralOrder(matrix), [1,2,3,4,8,12,11,10,9,5,6,7])


    def test3(self):
        sol = Solution()
        matrix = [
                    [1, 2, 3],
                    [5, 6, 7],
                    [9,10,11],
                    [4, 8, 12]
                    ]

        self.assertListEqual(sol.spiralOrder(matrix), [1,2,3,7,11,12,8,4,9,5,6,10])
    
       
if __name__ == "__main__":
    unittest.main()