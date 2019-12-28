'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []

        self.dfs(root, sum, cur, res)

        return res

    def dfs(self, node, target, cur, res):
        if node is None:
            return
        cur.append(node.val)
        if node.left is None and node.right is None and node.val == target:
            res.append(cur[:])
        else:
            newTarget = target - node.val
            self.dfs(node.left, newTarget, cur, res)
            self.dfs(node.right, newTarget, cur, res)
        cur.pop()



    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([5,4,8,11,None, 13, 4, 7, 2, None,None,5,1])
        print(sol.pathSum(root, 22))

if __name__ == "__main__":
    Solution.main() 
        