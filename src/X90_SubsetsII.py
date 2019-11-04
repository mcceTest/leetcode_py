'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''



class Solution(object):
    def subsetsWithDup2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        res = []
        cur = []
        nums.sort()
        used = [False] * len(nums)
        print(nums)
        self.dfs(nums, 0, used, cur, res)

        return res


    def dfs(self, nums, idx, used, cur, res):
        res.append(cur[:])

        if idx < len(nums):
            for i in range(idx, len(nums)):
                if not used[i]:
                    if i == 0 or (nums[i] != nums[i - 1]) or (used[i - 1]):
                        used[i] = True
                        cur.append(nums[i])
                        self.dfs(nums, i + 1, used, cur, res)
                        used[i] = False
                        cur.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        nums.sort()

        res = [[]]
        curIdx = 0
        cur = nums[0]
        curCount = 0

        while curIdx <= len(nums):
            if curIdx == len(nums) or nums[curIdx] != cur:
                preSize = len(res)
                for i in range(preSize):
                    tmp = res[i][:]
                    for _ in range(curCount):
                        tmp.append(cur)
                        res.append(tmp[:])

                if curIdx < len(nums):
                    cur = nums[curIdx]
                    curCount = 1
                curIdx += 1
            else:
                curCount += 1
                curIdx += 1

        return res
           
    @staticmethod
    def main():
        sol = Solution()
        nums = [1,2,2]

        print(sol.subsetsWithDup(nums))

        

if __name__ == "__main__":
    Solution.main() 
        