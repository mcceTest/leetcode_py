import unittest
from X150_EvaluateReversePolishNotation import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(sol.evalRPN(tokens), 9)


    def test2(self):
        sol = Solution()
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(sol.evalRPN(tokens), 6)

    def test3(self):
        sol = Solution()
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(sol.evalRPN(tokens), 22)

    def test4(self):
        sol = Solution()
        tokens = ["4","-2","/","2","-3","-","-"]
        self.assertEqual(sol.evalRPN(tokens), -7)

if __name__ == "__main__":
    unittest.main()