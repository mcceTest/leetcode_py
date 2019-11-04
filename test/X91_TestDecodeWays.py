import unittest
from X91_DecodeWays import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = '12'
        self.assertEqual(sol.numDecodings(s), 2)        


    def test2(self):
        sol = Solution()
        s = '226'
        self.assertEqual(sol.numDecodings(s), 3)   

    def test3(self):
        sol = Solution()
        s = '1'
        self.assertEqual(sol.numDecodings(s), 1)   
                                                        

if __name__ == "__main__":
    unittest.main()