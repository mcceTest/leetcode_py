'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   '''

from treeNode import TreeNode
import copy
   # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        if n <= 0:
           return []

        return self.helper(1, n)
         

    def helper(self, start, end):
        if start > end:
            return [None]
        elif start == end:
            return [TreeNode(start)]
        else:
            res = []
            for idx in range(start, end + 1):
                leftNodes = self.helper(start, idx - 1)
                rightNodes = self.helper(idx + 1, end)

                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        tmpRoot = TreeNode(idx)
                        tmpRoot.left = leftNode
                        tmpRoot.right = rightNode

                        res.append(tmpRoot)

            return res
   

    @staticmethod
    def main():
        sol = Solution()
        trees = sol.generateTrees(3)

        for tree in trees:
           print(tree)
        

if __name__ == "__main__":
    Solution.main() 