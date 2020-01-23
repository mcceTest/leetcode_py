'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        partitionList = self.calcPartitionList(s)
        print("pList:", partitionList)

        res = []
        curList = []
        self.dfs(s, partitionList, 0, curList, res)

        sRes = []
        for idxList in res:
            sList = []
            for i in range(len(idxList) - 1):
                sList.append(s[idxList[i]:idxList[i+1]])
            sRes.append(sList)

        return sRes

    def calcPartitionList(self, s):
        res = [ [] for _ in range(len(s))]
        for i in range(len(s)):
            res[i].append(i + 1)
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res[left].append(right + 1)
                left -= 1
                right += 1

        for i in range(len(s) - 1):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res[left].append(right + 1)
                left -= 1
                right += 1

        return res


    def dfs(self, s, pList, curIdx, curList, res):
        curList.append(curIdx)
        if curIdx == len(s):
            res.append(curList[:])
        else:
            for nextIdx in pList[curIdx]:
                self.dfs(s, pList, nextIdx, curList, res)
        curList.pop(-1)


    @staticmethod
    def main():
        sol = Solution()
        s = "aab"
        print(sol.partition(s))


if __name__ == "__main__":
    Solution.main() 