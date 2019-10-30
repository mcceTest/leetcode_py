'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

## 

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        nrow = len(matrix)
        if nrow == 0:
            return 0
        ncol = len(matrix[0])
        if ncol == 0:
            return 0

        curHeight = [0] * ncol
        res = 0

        for row in matrix:
            for i in range(ncol):
                if row[i] == '0':
                    curHeight[i] = 0
                else:
                    curHeight[i] += 1

            res = max(res, self.largestRectangleArea(curHeight))

        return res





    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        heights.append(-1)
        st = []
        res = 0
        for idx, height in enumerate(heights):
            while st and height <= heights[st[-1]]:
                cur = heights[st[-1]]
                st.pop()
                preIdx = -1
                if st:
                    preIdx = st[-1]

                res = max(res, cur * (idx - preIdx - 1))
            st.append(idx)

        

        return res

                


    @staticmethod
    def main():
        sol = Solution()
        matrix = [
                  ["1","0","1","0","0"],
                  ["1","0","1","1","1"],
                  ["1","1","1","1","1"],
                  ["1","0","0","1","0"]
                ]

        print(sol.maximalRectangle(matrix))

        

if __name__ == "__main__":
    Solution.main() 
      
        