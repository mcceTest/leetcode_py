'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []

        res = [ [0] * n for _ in range(n) ]

        cur = 1
        for layer in range(n // 2):
            for col in range(layer, n - 1 - layer):
                res[layer][col] = cur
                cur += 1

            for row in range(layer, n - 1 - layer):
                res[row][n - 1 - layer] = cur
                cur += 1

            for col in range(n - 1 - layer, layer, -1):
                res[n - 1 - layer][col] = cur 
                cur += 1

            for row in range(n - 1 - layer, layer, -1):
                res[row][layer] = cur
                cur += 1

        if n % 2 == 1:
            res[n // 2][n // 2] = n * n

        return res



    @staticmethod
    def main():
        sol = Solution()
        n = 3
        print(sol.generateMatrix(n))

if __name__ == "__main__":
    Solution.main() 