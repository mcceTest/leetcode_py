'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getHeight(root) >= 0


    def getHeight(self, node):
        if node is None:
            return 0

        leftHeight = self.getHeight(node.left)
        if leftHeight < 0:
            return -1

        rightHeight = self.getHeight(node.right)
        if rightHeight < 0:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1


        


    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        print(sol.isBalanced(root))

if __name__ == "__main__":
    Solution.main() 
        