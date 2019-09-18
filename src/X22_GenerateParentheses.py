'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        res = []

        left = right = n
        cur = ""
        self.dfs(left, right, cur, res)

        return res


    def dfs(self, left, right, cur, res):
        if left == 0 and right == 0:
            res.append(cur[:])
            return

        if left > 0:
            self.dfs(left - 1, right, cur + '(', res)

        if right > left:
            self.dfs(left, right - 1, cur + ')', res)


    @staticmethod
    def main():
        sol = Solution()

        print(sol.generateParenthesis(3))
        
        
if __name__ == "__main__":
    Solution.main()   