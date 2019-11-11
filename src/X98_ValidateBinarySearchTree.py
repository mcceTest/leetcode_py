'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
## TODO: Use inorder traversal
from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, -sys.maxsize - 1, sys.maxsize)

    def dfs(self, root, minLimit, maxLimit):
        if root is None:
            return True

        if root.val > minLimit and root.val < maxLimit and self.dfs(root.left, minLimit, root.val) and self.dfs(root.right, root.val, maxLimit):
            return True

        return False

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([5,1,4,None,None,3,6])
        print(sol.isValidBST(root))

if __name__ == "__main__":
    Solution.main() 