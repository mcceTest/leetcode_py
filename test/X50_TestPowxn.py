import unittest

from X50_Powxn import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        x = 2.00000
        n = 10

        self.assertAlmostEqual(sol.myPow(x, n), 1024)


    def test2(self):
        sol = Solution()
        x = 2.10000
        n = 3

        self.assertAlmostEqual(sol.myPow(x, n), 9.26100)

    def test3(self):
        sol = Solution()
        x = 2.00000
        n = -2

        self.assertAlmostEqual(sol.myPow(x, n), 0.25)

    
    
       
if __name__ == "__main__":
    unittest.main()