import unittest

from X67_AddBinary import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        a = "11"
        b = "1"

        self.assertEqual(sol.addBinary(a, b), '100')

    def test2(self):
        sol = Solution()
        a = "1010"
        b = "1011"

        self.assertEqual(sol.addBinary(a, b), '10101')
    

       
if __name__ == "__main__":
    unittest.main()