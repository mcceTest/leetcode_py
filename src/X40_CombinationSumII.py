'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        res = []
        curRes = []

        candidates.sort()

        # dfs search of the possible state space
        self.dfs(candidates, target, -1, 0, curRes, res)

        return res

        
    def dfs(self, candidates, target, idx, curTotal, curRes, res):
        if curTotal == target:
            res.append(curRes[:])
            return

        if idx >= len(candidates):
            return

        curIdx = idx + 1
        while curIdx < len(candidates):
            if curTotal + candidates[curIdx] <= target:
                curRes.append(candidates[curIdx])
                self.dfs(candidates, target, curIdx, curTotal + candidates[curIdx], curRes, res)
                curRes.pop(-1)
            else:
                break
            
            curIdx += 1
            while curIdx < len(candidates) and candidates[curIdx - 1] == candidates[curIdx]:
                curIdx += 1

    @staticmethod
    def main():
        sol = Solution()

        candidates = [2,3,6,7]
        target = 7

        print(sol.combinationSum2(candidates, target))
        

if __name__ == "__main__":
    Solution.main()  