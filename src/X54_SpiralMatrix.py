'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        nrow = len(matrix)
        if nrow == 0:
            return []
        ncol = len(matrix[0])
        if ncol == 0:
            return []

        res = []
        minLen = min(nrow, ncol)
        for row in range(minLen // 2):
            for col in range(row, ncol - row):
                res.append(matrix[row][col])

            for i in range(row + 1, nrow - row - 1):
                res.append(matrix[i][ncol - 1 - row])

            for col in range(ncol - 1 - row, row - 1, -1):
                res.append(matrix[nrow - 1 - row][col])

            for i in range(nrow - 2 - row, row, -1):
                res.append(matrix[i][row])

        if minLen % 2 == 1:
            if nrow <= ncol:
                for i in range(minLen // 2, ncol - minLen // 2):
                    res.append(matrix[minLen // 2][i])
            else:
                for i in range(minLen // 2, nrow - minLen // 2):
                    res.append(matrix[i][minLen // 2])

        
        return res

    @staticmethod
    def main():
        sol = Solution()
        matrix = [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]
                ]
        print(sol.spiralOrder(matrix))

if __name__ == "__main__":
    Solution.main() 