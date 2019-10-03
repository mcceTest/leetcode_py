'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if not candidates:
            return []

        res = []
        curRes = []

        # dfs search of the possible state space
        self.dfs(candidates, target, 0, 0, curRes, res)

        return res

        
    def dfs(self, candidates, target, idx, curTotal, curRes, res):
        if curTotal == target:
            res.append(curRes[:])
            return

        if idx >= len(candidates):
            return

        self.dfs(candidates, target, idx + 1, curTotal, curRes, res)

        if curTotal + candidates[idx] <= target:
            curRes.append(candidates[idx])
            self.dfs(candidates, target, idx, curTotal + candidates[idx], curRes, res)
            curRes.pop(-1)


        
    @staticmethod
    def main():
        sol = Solution()

        candidates = [2,3,6,7]
        target = 7

        print(sol.combinationSum(candidates, target))
        

if __name__ == "__main__":
    Solution.main()   