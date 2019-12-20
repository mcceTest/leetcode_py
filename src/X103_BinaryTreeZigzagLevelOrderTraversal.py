'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
    def zigzagLevelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        curNodes = [root]
        reversed = False

        while curNodes:
            curValues = []
            nextNodes = []
        
            for node in curNodes:
                curValues.append(node.val)
                if node.left is not None:
                    nextNodes.append(node.left)
                if node.right is not None:
                    nextNodes.append(node.right)

            if reversed:
                curValues.reverse()
                reversed = False
            else:
                reversed = True
            res.append(curValues)
            curNodes = nextNodes

        return res

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        self.dfs(root, 0, res)

        return res

    def dfs(self, node, level, res):
        if node is None:
            return

        if level >= len(res):
            res.append([node.val])
        else:
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
        
        self.dfs(node.left, level + 1, res)
        self.dfs(node.right, level + 1, res)
        
    

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([3,9,20,None,None,15,7])
        print(sol.zigzagLevelOrder(root))

if __name__ == "__main__":
    Solution.main() 