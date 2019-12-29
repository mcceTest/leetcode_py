'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution(object):
    def getRow2(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        cur = [1]
        for _ in range(rowIndex):
            nxt = [1] * (len(cur) + 1)
            for i in range(len(cur) - 1):
                nxt[i + 1] = cur[i] + cur[i + 1]
            cur = nxt

        return cur 

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        cur = [1]
        for _ in range(rowIndex):
            for i in range(len(cur) - 1, 0, -1):
                cur[i] += cur[i - 1]
            cur.append(1)            

        return cur 

    @staticmethod
    def main():
        sol = Solution()
        rowIndex = 3
        print(sol.getRow(rowIndex))


if __name__ == "__main__":
    Solution.main() 