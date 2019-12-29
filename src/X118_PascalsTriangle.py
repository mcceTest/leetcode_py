'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        cur = [1]
        for _ in range(numRows):
            res.append(cur[:])
            for i in range(len(cur) - 1, 0, -1):
                cur[i] += cur[i - 1]
            cur.append(1)

        return res

    @staticmethod
    def main():
        sol = Solution()
        numRows = 5
        print(sol.generate(numRows))


if __name__ == "__main__":
    Solution.main() 