import unittest

from X22_GenerateParentheses import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertListEqual(sorted(sol.generateParenthesis(3)), sorted([
                                                                        "((()))",
                                                                        "(()())",
                                                                        "(())()",
                                                                        "()(())",
                                                                        "()()()"
                                                                        ]))


        self.assertListEqual(sorted(sol.generateParenthesis(1)), sorted([
                                                                        "()",
                                                                        ]))

        self.assertListEqual(sorted(sol.generateParenthesis(2)), sorted([
                                                                        "()()",
                                                                        "(())"
                                                                        ]))
        

       
if __name__ == "__main__":
    unittest.main()