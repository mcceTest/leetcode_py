import unittest

from X58_LengthofLastWord import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "Hello World"
        self.assertEqual(sol.lengthOfLastWord(s), 5)
    

   
    
       
if __name__ == "__main__":
    unittest.main()