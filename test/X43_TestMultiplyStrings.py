import unittest

from X43_MultiplyStrings import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        num1 = "2"
        num2 = "3"

        self.assertEqual(sol.multiply(num1, num2), "6")


    def test2(self):
        sol = Solution()
        num1 = "123"
        num2 = "456"

        self.assertEqual(sol.multiply(num1, num2), "56088")
    
        
       
if __name__ == "__main__":
    unittest.main()