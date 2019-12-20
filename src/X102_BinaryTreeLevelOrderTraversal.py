'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

## TODO: run queue BFS 

from treeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        curNodes = [root]

        while curNodes:
            nextNodes = []
            curValues = []
            for node in curNodes:
                curValues.append(node.val)
                if node.left is not None:
                    nextNodes.append(node.left)
                if node.right is not None:
                    nextNodes.append(node.right)
            res.append(curValues)
            curNodes = nextNodes

        return res

        

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        print(sol.levelOrder(root))

if __name__ == "__main__":
    Solution.main() 