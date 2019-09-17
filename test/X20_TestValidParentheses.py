import unittest

from X20_ValidParentheses import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertTrue(sol.isValid("()"))

        self.assertTrue(sol.isValid("()[]{}"))

        self.assertTrue(sol.isValid("{[]}"))

        self.assertFalse(sol.isValid("(]"))

        self.assertFalse(sol.isValid("([)]"))
        
       
if __name__ == "__main__":
    unittest.main()