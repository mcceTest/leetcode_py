import unittest

from X32_LongestValidParentheses import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        s = "(()"
        self.assertEqual(sol.longestValidParentheses(s), 2)

    def test2(self):
        sol = Solution()

        s = ")()())"
        self.assertEqual(sol.longestValidParentheses(s), 4)

        
       
if __name__ == "__main__":
    unittest.main()