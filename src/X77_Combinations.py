'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []
        res = []

        used = [False] * (n + 1)

        self.dfs(n, k, 0, used, res, result)

        return result


    def dfs(self, n, k, idx, used, res, result):
        if idx == k:
            result.append(res[:])
            return

        start = 1 if len(res) == 0 else res[-1] + 1
        end = n - (k - 1 - idx)
        for i in range(start, end + 1):
            if not used[i]:
                res.append(i)
                used[i] = True
                self.dfs(n, k, idx + 1, used, res, result)
                used[i] = False
                res.pop(-1)


    @staticmethod
    def main():
        sol = Solution()
        n = 4
        k = 2
        print(sol.combine(n, k))

if __name__ == "__main__":
    Solution.main()   