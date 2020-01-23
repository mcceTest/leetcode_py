'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
import collections

## TODO: use dp
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0

        pList = self.calcPartitionList(s)

        return self.bfs(s, 0, len(s), pList)

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


    def bfs(self, s, start, end, pList):
        q = collections.deque()
        q.append(start)
        curLen = 0
        visited = set()
        visited.add(start)

        while q:
            qz = len(q)
            for _ in range(qz):
                curIdx = q.popleft()
                for neigb in pList[curIdx]:
                    if neigb not in visited:
                        if neigb == end:
                            return curLen
                        visited.add(neigb)
                        q.append(neigb)

            curLen += 1

        return len(s) - 1
        

    @staticmethod
    def main():
        sol = Solution()
        s = "aab"
        print(sol.minCut(s))


if __name__ == "__main__":
    Solution.main() 