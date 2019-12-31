'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxSum = None

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = None
        if root is None:
            return 0

        self.dfs(root)
        return self.maxSum


    def dfs(self, node):
        '''
        max sum going down from this node (inclusive)
        '''

        if node is None:
            return 0

        maxSum = node.val
        leftSum = 0
        if node.left is not None:
            leftSum = max(0, self.dfs(node.left))
            
        rightSum = 0
        if node.right is not None:
            rightSum = max(0, self.dfs(node.right))

        nodeSum = node.val + max(leftSum, rightSum)

        maxSum = max(maxSum, node.val + leftSum + rightSum)
        if self.maxSum is None:
            self.maxSum = maxSum
        else:
            self.maxSum = max(maxSum, self.maxSum)

        return nodeSum

    def dfs2(self, node):
        if node is None:
            return (0, 0)

        maxSum = node.val
        leftSum = 0
        if node.left is not None:
            leftSum, leftMax = self.dfs2(node.left)
            maxSum = max(maxSum, leftMax)
            leftSum = max(0, node.left.val + leftSum)

        rightSum = 0
        if node.right is not None:
            rightSum, rightMax = self.dfs2(node.right)
            maxSum = max(maxSum, rightMax)
            rightSum = max(0, node.right.val + rightSum)

        maxSum = max(maxSum, node.val + leftSum + rightSum)

        return (max(leftSum, rightSum), maxSum)


    def maxPathSum2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs2(root)[1]
    


    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([-3])
        print(sol.maxPathSum(root))


if __name__ == "__main__":
    Solution.main() 
        


