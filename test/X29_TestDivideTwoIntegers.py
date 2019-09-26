import unittest

from X29_DivideTwoIntegers import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        dividend = 10
        divisor = 3

        self.assertEqual(sol.divide(dividend, divisor), 3)


    def test2(self):
        sol = Solution()

        dividend = 7
        divisor = -3

        self.assertEqual(sol.divide(dividend, divisor), -2)


    def test3(self):
        sol = Solution()

        dividend = 2
        divisor = -3

        self.assertEqual(sol.divide(dividend, divisor), 0)

    def test4(self):
        sol = Solution()

        dividend = - 2 ** 31
        divisor = -1

        self.assertEqual(sol.divide(dividend, divisor), 2 ** 31 - 1)


    def test5(self):
        sol = Solution()

        dividend = 2147483647
        divisor = 1

        self.assertEqual(sol.divide(dividend, divisor), 2147483647)
        
       
if __name__ == "__main__":
    unittest.main()