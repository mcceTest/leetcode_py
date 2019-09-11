import unittest
from X7_ReverseInteger import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.reverse(123), 321)

        self.assertEqual(sol.reverse(-123), -321)
        
        self.assertEqual(sol.reverse(120), 21)

        self.assertEqual(sol.reverse(0), 0)


if __name__ == "__main__":
    unittest.main()