'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        cached = [0] * (n + 1)
        cached[0] = cached[1] = 1

        for idx in range(2, n + 1):
            for left in range(idx):
                cached[idx] += (cached[left] * cached[idx - 1 - left])


        return cached[n]

    @staticmethod
    def main():
        sol = Solution()
        print(sol.numTrees(3))
        

if __name__ == "__main__":
    Solution.main() 