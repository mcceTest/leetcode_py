'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

'''



class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[-1]:
            return 0
        
        costList = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                costList[j] = triangle[i][j] + min(costList[j], costList[j + 1])

        return costList[0]

    @staticmethod
    def main():
        sol = Solution()
        triangle = [
                        [2],
                        [3,4],
                    [6,5,7],
                    [4,1,8,3]
                    ]

        print(sol.minimumTotal(triangle))


if __name__ == "__main__":
    Solution.main() 